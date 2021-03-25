import psycopg2
import os
import json
from datetime import datetime, timezone, tzinfo
import pytz
import requests

env = os.environ

fail_count = 0

while True:
    try:
        conn = psycopg2.connect(dbname=env['POSTGRES_DB'], user=env['POSTGRES_USER'], host='postgres', port=5432, password=env['POSTGRES_PASSWORD'])
        cur = conn.cursor()
        # requirements for tcss object creation is in analytics.mutations
        ### NOTE: later on, make it so that verified email is required for tcss

        # only creates tcss object if meets requirements, on SiteVisit object creation.

        # vu = valid users, ivu = invalid users
        ### NOTE: in the graphql query for who to follow, if tcss_wtf is length zero, 
        # users = User.objects.filter(settings__has_tcss=True)
        # candidates = users.order_by('-settings__tri_count')[:100]
        # use above code to get trending and just return that, paginated


        # TODO: actually... we could make our algorithm a lot more efficient with that.. if who to 
        # follow is a cap of 120 ppl, some can be people who's profile you've looked at before 
        # but don't follow and the rest are following's following's thing
        # if we can't fill up 120 with those 2 groups, get remaining from trending list

        cur.execute("""SELECT user_id FROM tcss_tcss;""")
        vu = cur.fetchall()
        for i, row in enumerate(vu):
            # NOTE: for snippet, either one of the fields or it just says "Likes Computer Prgoramming"
            print('~~~~~~~~~~~~~~~')
            user_id = row[0]
            print(user_id)
            # for one deep, randomly select 10 following
            cur.execute("""SELECT followee_id FROM follows_follow WHERE follower_id = %s;""", (user_id,))
            following = cur.fetchall()
            print(following)
            cur.execute("""SELECT followee_id FROM follows_follow WHERE follower_id = %s ORDER BY random() LIMIT 10;""", (user_id,))
            following_one_deep = cur.fetchall()
            following_two_deep = {
                'candidates': []
            }
            following_two_deep_ids = ()
            for followee_one_deep_row in following_one_deep:
                followee_one_deep = followee_one_deep_row[0]
                # COMPLETED ✅: going through following's following will be very expensive and must be
                # changed later on - CHANGE OF PLANS - getting first 30 instead so it should be fine
                # COMPLETED ✅: order by popularity with tri_count
                # MONEY TODO: NOTE: when we implement the payment plans, we'll make it so that this query sorts by hasp_PLAN_NAME and hasp_SPF, so whoever payed for the plan to get suggested in who to follow have priority and are at the top
                # MONEY TODO: NOTE: however for any spots that are left over and need to be filled from trending can instead by filled by randomly selecting people who pay for suggested
                # GAURANTEE a spot for wtf payers, if more wtf payers than 120, randomly select 120
                # COMPLETED ✅: JOIN THE USERS TABLE WITH THIS THE SAME WAY AS USER SETTINGS AND SELECT USERNAME, FIRST NAME, LASTNAME AS WELL
                cur.execute("""SELECT followee_id, username, first_name, last_name FROM follows_follow as f JOIN users_usersettings AS s on s.user_id = f.followee_id JOIN users_user AS u on u.id = f.followee_id WHERE f.follower_id = %s ORDER BY s.tri_count DESC LIMIT 30;""", (followee_one_deep,))
                following_two_deep_one = cur.fetchall()
                # COMPLETED ✅: for each person check if user already follows them and that at least 1 interest tag is in common, if so, pop from list.
                # NOTE: in future, sort by similarity of interest tags
                cur.execute("""SELECT interest_tags FROM users_userprofile WHERE user_id = %s;""", (user_id,))
                user_it = cur.fetchall()
                for following_two_deep_one_row in following_two_deep_one:
                    followee_two_deep = following_two_deep_one_row[0]
                    if followee_two_deep != user_id:
                        cur.execute("""SELECT interest_tags FROM users_userprofile WHERE user_id = %s;""", (followee_two_deep,))
                        followee_two_deep_it = cur.fetchall()
                        print(followee_two_deep_it[0][0], followee_two_deep, user_it[0][0])
                        print('-----it------')
                        if not set(followee_two_deep_it[0][0]).isdisjoint(user_it[0][0]):
                            if not followee_two_deep in following_two_deep:
                                if not (followee_two_deep,) in following:
                                    # NOTE: Need to make this a foreign key instead of raw string
                                    candidate = {
                                        'id': followee_two_deep,
                                        'username': following_two_deep_one_row[1],
                                        'first_name': following_two_deep_one_row[2],
                                        'last_name': following_two_deep_one_row[3]
                                    }
                                    following_two_deep['candidates'].append(candidate)
                                    following_two_deep_ids += (followee_two_deep,)
            # print(following_two_deep, len(following_two_deep['candidates']))
            # NOTE: in graphql mutation, json.loads wtf and if length of candidates is less than 0, fill with trending
            
            if len(following_two_deep['candidates']) > 0:
                leftover = 120 - len(following_two_deep['candidates'])
                if leftover > 0:
                    cur.execute("""SELECT u.id, username, first_name, last_name FROM users_user AS u JOIN users_usersettings AS s on s.user_id = u.id WHERE u.id NOT IN %s ORDER BY s.tri_count DESC LIMIT %s;""", (following_two_deep_ids, str(leftover)))
                    trending_fetch = cur.fetchall()
                    keys = ('id', 'username', 'first_name', 'last_name')
                    trending = [dict(zip(keys, values)) for values in trending_fetch]
                    following_two_deep['candidates'] += trending
                    # print(following_two_deep, len(following_two_deep['candidates']))
                ####################
                # COMPLETED ✅: DO THE PART WHERE WE GET PPL YOU'VE LOOKED AT > 2 TIMES THAT YOU DONT FOLLOW
                # get max of 5, put 1 at 3rd position, another at 5th position, rest 9, 12, 15
                # NOTE: only bring recent matches and prioritize interests similarity
                ####################
                cur.execute("""SELECT viewee_id, username, first_name, last_name, COUNT(viewee_id) as vcount FROM analytics_profilevisit JOIN users_user AS u ON u.id = viewee_id WHERE viewer_id = %s AND viewee_id NOT IN (SELECT followee_id FROM follows_follow WHERE followee_id = viewee_id) GROUP BY viewee_id, username, first_name, last_name ORDER BY vcount DESC LIMIT 5;""", (user_id,))
                history_matches = cur.fetchall()
                print('matches::::', history_matches)
                for j, match in enumerate(history_matches):
                    if history_matches[j]:
                        candidate = {
                            'id': history_matches[j][0],
                            'username': history_matches[j][1],
                            'first_name': history_matches[j][2],
                            'last_name': history_matches[j][3]
                        }
                        if not candidate in following_two_deep['candidates']:
                            # COMPLETED ✅: make it append at specific locations, described above
                            if j is 0: following_two_deep['candidates'].insert(2, candidate)
                            if j is 1:following_two_deep['candidates'].insert(4, candidate)
                            if j is 2:following_two_deep['candidates'].insert(8, candidate)
                            if j is 3:following_two_deep['candidates'].insert(11, candidate)
                            if j is 4:following_two_deep['candidates'].insert(14, candidate)
                print('final print test:', following_two_deep, len(following_two_deep['candidates']))
            cur.execute("""UPDATE tcss_tcss SET wtf = %s WHERE user_id = %s;""", (json.dumps(following_two_deep), user_id))
            conn.commit()
            print('~~~~~~~~~~~~~~')
        break ## NOTE: delete this for prod lol
    except:
        fail_count += 1
        print("UNABLE TO CONNECTT!tt!t!~~~~~~")

        if fail_count > 150:
            print('something seriously uncool happened :(')
            break
print('broke loop!')

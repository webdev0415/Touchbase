import psycopg2
import os
import json
import traceback
from datetime import datetime, timezone, tzinfo
import pytz
import requests

# fe_1d = followee_one_deep
# fi_1d = following_one_deep
# fe_1d_r = followee_one_deep_row
# fe_2d = followee_two_deep
# fi_2d = following_two_deep
# fi_2d_ids = following_two_deep_ids
# fi_2d_1 = following_two_deep_one
# fi_2d_1r = following_two_deep_one_row
# hm = history_matches
# hml = history_matches_list
# ec_final = exp_cliques_final
# ep_final = exp_people_final
# w_final = wtf_final

env = os.environ

fail_count = 0

while True:
    try:
        # NOTE: USER AUTOCOMMIT = TRUE
        conn = psycopg2.connect(dbname=env['POSTGRES_DB'], user=env['POSTGRES_USER'], host='postgres', port=5432, password=env['POSTGRES_PASSWORD'])
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute("""SELECT user_id FROM tcss_tcss;""")
        vu = cur.fetchall()
        # for row in valid users, need this for explore*
        for i, row in enumerate(vu):
            print('~~~~~~~~~~~~~~~')
            user_id = row[0]
            print(user_id)

            # explore vars
            exp_cliques = []
            cur.execute("""SELECT interest_tags FROM users_userprofile WHERE user_id = %s;""", (user_id,))
            user_it = cur.fetchall()

            cur.execute("""SELECT id from tcss_tcss WHERE user_id = %s;""", (user_id,))
            user_tcss = cur.fetchall()[0][0]

            print('---------wtf----------')
            #  wtf vars
            cur.execute("""SELECT followee_id FROM follows_follow WHERE follower_id = %s ORDER BY random() LIMIT 10;""", (user_id,))
            following_one_deep = cur.fetchall()
            following_two_deep = []
            following_two_deep_ids = ()
            for followee_one_deep_row in following_one_deep:
                followee_one_deep = followee_one_deep_row[0]
                # NOTE: include exlcusion of already following/duplicates IN THE query
                # EXPLORE SECTION: will need to crawl following's cliques, currently in 1st depth loop.
                # 10 selected, so then choose a max of 5 from each and remove duplicates at very end. 
                # ^^^ cliques global var
                cur.execute("""SELECT clique_id FROM cliques_clique_members WHERE user_id = %s AND clique_id NOT IN (SELECT clique_id FROM cliques_clique_members WHERE user_id = %s) LIMIT 5;""", (followee_one_deep, user_id))
                exp_cliques.extend(cur.fetchall())

                cur.execute("""SELECT followee_id FROM follows_follow as f JOIN users_usersettings AS s on s.user_id = f.followee_id WHERE f.follower_id = %s AND followee_id NOT IN (SELECT followee_id FROM follows_follow WHERE follower_id = %s) AND followee_id != %s ORDER BY s.tri_count DESC LIMIT 30;""", (followee_one_deep, user_id, user_id))
                following_two_deep_one = cur.fetchall()
                
                for following_two_deep_one_row in following_two_deep_one:
                    followee_two_deep = following_two_deep_one_row[0]
                    if not followee_two_deep in following_two_deep:
                        following_two_deep.append(following_two_deep_one_row)
                        following_two_deep_ids += (followee_two_deep,)

            
            if len(following_two_deep) > 0:
                leftover = 45 - len(following_two_deep)
                # NOTE: in graphql, if wtf_exp length is 0, then return GD (global default)
                if leftover > 0:
                    cur.execute("""SELECT u.id FROM users_user AS u JOIN users_usersettings AS s on s.user_id = u.id WHERE u.id NOT IN %s AND u.id NOT IN (SELECT followee_id FROM follows_follow WHERE follower_id = %s) AND u.id != %s ORDER BY s.tri_count DESC LIMIT %s;""", (following_two_deep_ids, user_id, user_id, str(leftover)))
                    following_two_deep.append(cur.fetchall()[0])
                
                cur.execute("""SELECT viewee_id, COUNT(viewee_id) as vcount FROM analytics_profilevisit WHERE viewer_id = %s AND viewee_id NOT IN %s AND viewee_id NOT IN (SELECT followee_id FROM follows_follow WHERE follower_id = viewee_id) GROUP BY viewee_id ORDER BY vcount DESC LIMIT 5;""", (user_id, following_two_deep_ids))
                history_matches = cur.fetchall()
                for j, match in enumerate(history_matches):
                    if history_matches[j]:
                        # formatting below
                        hml = list(history_matches[j])
                        del hml[-1]
                        cand_id = tuple(hml)
                        if j is 0:following_two_deep.insert(2, cand_id)
                        if j is 1:following_two_deep.insert(4, cand_id)
                        if j is 2:following_two_deep.insert(8, cand_id)
                        if j is 3:following_two_deep.insert(11, cand_id)
                        if j is 4:following_two_deep.insert(14, cand_id)
                print('before test:', following_two_deep, len(following_two_deep))
                
                # get list into correct format
                wtf_final = []
                for t in following_two_deep:
                    t = (user_tcss,) + t
                    if t not in wtf_final:
                        wtf_final.append(t)
                print('final print test:', str(wtf_final).lstrip('[').rstrip(']'), len(wtf_final))

                cur.execute("""DELETE from tcss_tcss_wtf WHERE tcss_id = %s;""", (user_tcss,))
                # NOTE: make sure it's in right order, sort it by tcss_tcss_wtf.id ASCENDING
                # SELECT * FROM tcss_tcss_wtf WHERE tcss_id = 8 ORDER BY id ASC;
                sql = f"""INSERT INTO tcss_tcss_wtf (tcss_id, user_id) VALUES {str(wtf_final).lstrip('[').rstrip(']')};"""
                cur.execute(sql)
            print('~~~~~~~~~~~~~~')




            print('---------explore----------')
            # use RAKE instead of summa for any scraping.
            
            # explore is going to be people, brands, and cliques right?
            # ~
            # but it will be separate from wtf in the way that wtf is basically a following crawler and and explore will be an interest matcher but pull all it's candidates from trending
            # ~
            # now that's for people & brands
            # ~
            # for cliques, i'll get 60% from crawling following and other 40% from trending cliques
            # ~
            # boom, explore is fully planned

            # cliques is ready, if less than 50, fill with top trending cliques until reaches 50.
            if len(exp_cliques) < 50:
                cid_list = []
                for t in exp_cliques:
                    cid_list.append(t[0])
                cur.execute("""SELECT id FROM cliques_clique WHERE id NOT IN %s AND id NOT IN (SELECT clique_id FROM cliques_clique_members WHERE user_id = %s) ORDER BY tri_count DESC LIMIT %s;""", (tuple(cid_list), user_id, str(50 - len(exp_cliques)),))
                exp_cliques.extend(cur.fetchall())

            # get 100 ppls from trending with similar interests. 
            cur.execute("""SELECT u.id FROM users_user AS u JOIN users_usersettings AS s ON s.user_id = u.id JOIN users_userprofile AS p ON p.user_id = u.id WHERE p.interest_tags && %s AND u.id != %s AND u.id NOT IN (SELECT followee_id FROM follows_follow WHERE follower_id = %s) ORDER BY s.tri_count DESC LIMIT 100;""", ('{' + ",".join(user_it[0][0]) + '}', user_id, user_id))
            exp_people = cur.fetchall()
            # get 25 brands. users_id from users_usersettings where is_business = true, and hasp_PROMOTED = True,
            # only need 1 match for day1. select where overlap = true, limit of 25.

            exp_cliques_final = []
            for t in exp_cliques:
                t = (user_tcss,) + t
                exp_cliques_final.append(t)
            print(exp_cliques_final)
            cur.execute("""DELETE from tcss_tcss_exp_cliques WHERE tcss_id = %s;""", (user_tcss,))
            sql = f"""INSERT INTO tcss_tcss_exp_cliques (tcss_id, clique_id) VALUES {str(exp_cliques_final).lstrip('[').rstrip(']')};"""
            cur.execute(sql)

            exp_people_final = []
            for t in exp_people:
                t = (user_tcss,) + t
                exp_people_final.append(t)
            print(exp_people_final)
            cur.execute("""DELETE from tcss_tcss_exp_people WHERE tcss_id = %s;""", (user_tcss,))
            sql = f"""INSERT INTO tcss_tcss_exp_people (tcss_id, user_id) VALUES {str(exp_people_final).lstrip('[').rstrip(']')};"""
            cur.execute(sql)

            # NOTE: sorted by overlap/intersection count of interests, limit of 25
            # use intarray postgres plugin to sort by the count of overlap.
            # businesses can build an interest profile for their target audience and TB will
            # automagically find THE best candidates for you. 
            

            # ManyToMany on UserTCSS. So each exp_cl, exp_pf, exp_br can have many Clique, UserProfile, and Brand,
            # AND each Clique, UserProfile, and Brand can be in many user's TCSS.
            # NOTE: do same with wtf in terms of the many to many stuff.
            # return 3 lists to frontend, frontend sorts based off vuetify brekapoint size


            # since we're combining wtf and explore scripts, at the point where i select 10 random followed users, im also selecting up to 5 cliques from each of them. If in the end it turns out less than 50, fill with top trending cliques until reaches 50. 
            # ~
            # then get 100 ppls from trending with at least 1 interest in common 
            # ~
            # then get 25 brands. select profiles where is_business = true and at least 1 interest tag in common, and sort by hasp_(NAME_OF_EXPLORE_PROMOTION_PLAN)
            # ~
            # idk how efficient the above query will be, but yeah. that business' tags won't be their actual profile ones, it'll be tags they choose specifically for the kind of users they wanna target. In there future we can enhance this by making the query sort by overlap count of the interest tags, meaning sorted by the MOST similar instead of only needing at least 1 match
            # ~
            # on desktop, this will average out to: 2 profiles on every row, 1 clique on every row, and 1 brand on every other row
            # ~
            # on phone, for every 3 rows it averages to 2 profiles, 1 clique, and 0.5 brands.  if it happens to be that there won't be a brand in that group, then it's only 2 rows (im thinking on phone we should have a brand take up full width, like a clique)
        
        break ## NOTE: delete this for prod lol
    except:
        fail_count += 1
        print("UNABLE TO CONNECTT!tt!t!~~~~~~")
        print(traceback.format_exc())

        if fail_count > 100:
            print('something seriously uncool happened :(')
            break
print('broke loop!')

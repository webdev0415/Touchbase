import psycopg2
import os
import json
import traceback
from datetime import datetime, timezone, tzinfo
import pytz
import requests

# VARIABLES GUIDE
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
        # setup conn
        conn = psycopg2.connect(dbname=env['POSTGRES_DB'], user=env['POSTGRES_USER'], host='postgres', port=5432, password=env['POSTGRES_PASSWORD'])
        conn.autocommit = True
        cur = conn.cursor()
        # select all users who are tcss valid (vu = valid users)
        cur.execute("""SELECT user_id FROM tcss_tcss;""")
        vu = cur.fetchall()

        for i, row in enumerate(vu):
            user_id = row[0]

            # explore variables. cliques, user interest tags, tcss_id 
            exp_cliques = []
            cur.execute("""SELECT interest_tags FROM users_userprofile WHERE user_id = %s;""", (user_id,))
            user_it = cur.fetchall()
            cur.execute("""SELECT id from tcss_tcss WHERE user_id = %s;""", (user_id,))
            user_tcss = cur.fetchall()[0][0]

            #  wtf vars
            cur.execute("""SELECT followee_id FROM follows_follow WHERE follower_id = %s ORDER BY random() LIMIT 10;""", (user_id,))
            fi_1d = cur.fetchall()
            fi_2d = []
            # makes it simple to check NOT IN for queries.
            fi_2d_ids = ()
            for fe_1d_r in fi_1d:
                fe_1d = fe_1d_r[0]
                cur.execute("""SELECT clique_id FROM cliques_clique_members WHERE user_id = %s AND clique_id NOT IN (SELECT clique_id FROM cliques_clique_members WHERE user_id = %s) LIMIT 5;""", (fe_1d, user_id))
                exp_cliques.extend(cur.fetchall())

                cur.execute("""SELECT followee_id FROM follows_follow as f JOIN users_usersettings AS s on s.user_id = f.followee_id WHERE f.follower_id = %s AND followee_id NOT IN (SELECT followee_id FROM follows_follow WHERE follower_id = %s) AND followee_id != %s ORDER BY s.tri_count DESC LIMIT 30;""", (fe_1d, user_id, user_id))
                fi_2d_1 = cur.fetchall()
                
                for fi_2d_1r in fi_2d_1:
                    fe_2d = fi_2d_1r[0]
                    if not fe_2d in fi_2d:
                        fi_2d.append(fi_2d_1r)
                        fi_2d_ids += (fe_2d,)
            
            if len(fi_2d) > 0:
                leftover = 120 - len(fi_2d)
                if leftover > 0:
                    cur.execute("""SELECT u.id FROM users_user AS u JOIN users_usersettings AS s on s.user_id = u.id WHERE u.id NOT IN %s AND u.id NOT IN (SELECT followee_id FROM follows_follow WHERE follower_id = %s) AND u.id != %s ORDER BY s.tri_count DESC LIMIT %s;""", (fi_2d_ids, user_id, user_id, str(leftover)))
                    fi_2d.append(cur.fetchall()[0])
                
                cur.execute("""SELECT viewee_id, COUNT(viewee_id) as vcount FROM analytics_profilevisit WHERE viewer_id = %s AND viewee_id NOT IN %s AND viewee_id NOT IN (SELECT followee_id FROM follows_follow WHERE follower_id = viewee_id) GROUP BY viewee_id ORDER BY vcount DESC LIMIT 5;""", (user_id, fi_2d_ids))
                hm = cur.fetchall()
                for j, match in enumerate(hm):
                    if hm[j]:
                        # formatting below
                        hml = list(hm[j])
                        del hml[-1]
                        cand_id = tuple(hml)
                        # insert at certain locations of list
                        if j is 0:fi_2d.insert(2, cand_id)
                        if j is 1:fi_2d.insert(4, cand_id)
                        if j is 2:fi_2d.insert(8, cand_id)
                        if j is 3:fi_2d.insert(11, cand_id)
                        if j is 4:fi_2d.insert(14, cand_id)
                
                # get list into correct format
                w_final = []
                for t in fi_2d:
                    t = (user_tcss,) + t
                    w_final.append(t)
                cur.execute("""DELETE from tcss_tcss_wtf WHERE tcss_id = %s;""", (user_tcss,))
                sql = f"""INSERT INTO tcss_tcss_wtf (tcss_id, user_id) VALUES {str(w_final).lstrip('[').rstrip(']')};"""
                cur.execute(sql)

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

            ec_final = []
            for t in exp_cliques:
                t = (user_tcss,) + t
                ec_final.append(t)
            cur.execute("""DELETE from tcss_tcss_exp_cliques WHERE tcss_id = %s;""", (user_tcss,))
            sql = f"""INSERT INTO tcss_tcss_exp_cliques (tcss_id, clique_id) VALUES {str(ec_final).lstrip('[').rstrip(']')};"""
            cur.execute(sql)

            ep_final = []
            for t in exp_people:
                t = (user_tcss,) + t
                ep_final.append(t)
            cur.execute("""DELETE from tcss_tcss_exp_people WHERE tcss_id = %s;""", (user_tcss,))
            sql = f"""INSERT INTO tcss_tcss_exp_people (tcss_id, user_id) VALUES {str(ep_final).lstrip('[').rstrip(']')};"""
            cur.execute(sql)
        break ## NOTE: delete this for prod lol
    except:
        fail_count += 1
        print("~~~~~~UNABLE TO CONNECTT!tt!t!~~~~~~")
        print(traceback.format_exc())

        if fail_count > 100:
            print('something seriously uncool happened :(')
            break
print('Program has been exited.')

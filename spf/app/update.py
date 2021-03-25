import psycopg2
import os
import json
from datetime import datetime, timezone, tzinfo
import pytz
import requests

env = os.environ

oafs = {
    'youtube': {
        'key': env['YOUTUBE_AK'],
        'client_id': env['YOUTUBE_CID'],
        'secret': env['YOUTUBE_CS'],
        'api_url': ''
    }
}

test_oaf_supported = [
    'youtube',
]

# GRAPHQL AND REDIS IDEAS HAVE BOTH BEEN CANCELLED, WORKS DIRECTLY WITH DB NOW
# test.py
### CONNECT TO REDIS - cancelled
### IF IN USER FOR LOOP, IF ON LAST ITEM OF LIST,
### APPEND THE ITEM ID TO THE REDIS LIST "SPFL_ID" FOR
### THE LAST POST IN THAT FETCH. 
# django
### NOW WHEN FETCHING POSTS
### IN DJANGO, GET ALL POSTS WHERE USER=USER AND
### ID >= PY_SPFL_ID VARIABLE FROM SETTINGS.PY BOOM BOOM

### This specifies the default fetching mechanism for last 12hr. However, when needing older posts,

### a) - PAGINATION:
    # IF SCROLLING DOWN AND NEED MORE, TAKE LAST INDEX OF SPFL_ID + (PAGE_COUNT - 1)
### b) - CUSTOM RANGE:
    # SEPERATE GRAPHQL QUERY THAT TAKES IN TIME RANGE + OTHER ARGS AND FILTERS FROM DB
    # BASED OFF TIME OPERATIONS FROM created FIELD OF POST OBJECT

### OPTIMIZATION:
    ## new (graphql):
        # When very last item is reached, send graphql request with that post id as parameter
        # That graphql mutation takes id param and appends to settings.py's global SPFL_ID list

    # Instead of reaching out to redis for every request, have PY_SPFL_ID variable in settings
    # Settings.py connected to redis, subscribed to changes of SPFL_ID. PY_SPFL_ID is equal to
    # latest value of SPFL_ID.
    ## Whenever SPFL_ID gets updated, settings.py finds out and then updates PY_SPFL_ID to the latest value of SPFL_ID.

try:
    conn = psycopg2.connect(dbname=env['POSTGRES_DB'], user=env['POSTGRES_USER'], host='postgres', port=5432, password=env['POSTGRES_PASSWORD'])
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""SELECT user_id FROM users_usersettings WHERE "haspSPF" = TRUE;""")
    u_haspSPF = cur.fetchall()
    for iu, row in enumerate(u_haspSPF):
        print('----------------')
        user_id = row[0]
        print(user_id)
        cur.execute("""SELECT * FROM accounts_account WHERE user_id = %s;""", (user_id,)) ###
        a_u_haspSPF = cur.fetchall()
        ## possible optimization: if has any accounts that are OAF supported OR if has any accounts that are SPF enabled
        print(iu == len(u_haspSPF) - 1)
        if iu != len(u_haspSPF) - 1: ### NOT LAST USER IN LIST
            # for account in accounts of that user
            for a_row in a_u_haspSPF:
                print('<account>')
                if a_row[-1]:
                    norm = a_row[-4][0:a_row[-4].find('.')] if a_row[-4].count('.') == 1 else a_row[-4].split('.')[1]
                    print(norm)
                    if norm in oafs:
                        print('~~~ 1111API FETCHING WOULD BE DONE HERE! ~~~')
                        if norm == 'youtube':
                            ### GET SPFServiceID WHERE id=user_id THEN GET VALUE OF youtube FIELD, ChannelID
                            cur.execute("""SELECT youtube FROM users_spfserviceid WHERE user_id = %s;""", (user_id,))
                            # chid = 'UC-lHJZR3Gqxm24_Vd_AJ5Yw' <-- pewdiepie
                            chid = cur.fetchone()[0]
                            print(chid, user_id, norm)
                            result = requests.get(f"https://www.googleapis.com/youtube/v3/search?key={oafs[norm]['key']}&channelId={chid}&part=snippet&order=date&maxResults=20")
                            r = result.json()['items']
                            utc = pytz.utc
                            now = datetime.utcnow().replace(tzinfo=utc)
                            for ip, post in enumerate(r):
                                cur.execute("""INSERT INTO users_oauthpost (created, service, pdj, user_id) VALUES (%s, %s, %s, %s);""", (now, norm, json.dumps(post), user_id))
                                # conn.commit()
                    else:
                        print('This service is not yet supported for API Integration.')
                else:
                    print('Share SPF disabled')
                print('</account>')
        else:  ### LAST USER IN LIST
            for ia, a_row in enumerate(a_u_haspSPF):
                if ia != len(a_u_haspSPF) - 1: ### if not last item
                    print('<account>')
                    print(a_row[-1])
                    if a_row[-1]:
                        norm = a_row[-3][0:a_row[-3].find('.')] if a_row[-3].count('.') == 1 else a_row[-3].split('.')[1]
                        print(norm)
                        if norm in oafs:
                            print('~~~ 3333API FETCHING WOULD BE DONE HERE! ~~~')
                            if norm == 'youtube':
                                ### GET SPFServiceID WHERE id=user_id THEN GET VALUE OF youtube FIELD, ChannelID
                                cur.execute("""SELECT youtube FROM users_spfserviceid WHERE user_id = %s;""", (user_id,))
                                # chid = 'UC-lHJZR3Gqxm24_Vd_AJ5Yw' <-- pewdiepie
                                chid = cur.fetchone()[0]
                                print(chid, user_id, norm)
                                result = requests.get(f"https://www.googleapis.com/youtube/v3/search?key={oafs[norm]['key']}&channelId={chid}&part=snippet&order=date&maxResults=20")
                                r = result.json()['items']
                                utc = pytz.utc
                                now = datetime.utcnow().replace(tzinfo=utc)
                                for ip, post in enumerate(r):
                                    cur.execute("""INSERT INTO users_oauthpost (created, service, pdj, user_id) VALUES (%s, %s, %s, %s);""", (now, norm, json.dumps(post), user_id))
                                    # conn.commit()
                        else:
                            print('This service is not yet supported for API Integration.')
                    else:
                        print('Share SPF disabled')
                    print('</account>')
                else:
                    print('<account>')
                    if a_row[-1]:
                        r_svc = a_row[-4]
                        norm = r_svc[0:r_svc.find('.')] if r_svc.count('.') == 1 else r_svc.split('.')[1]
                        print(norm)
                        if norm in oafs:
                            print('~~~ 2222API FETCHING WOULD BE DONE HERE! ~~~')
                            if norm == 'youtube':
                                ### GET SPFServiceID WHERE id=user_id THEN GET VALUE OF youtube FIELD, ChannelID
                                cur.execute("""SELECT youtube FROM users_spfserviceid WHERE user_id = %s;""", (user_id,))
                                # chid = 'UC-lHJZR3Gqxm24_Vd_AJ5Yw' <-- pewdiepie
                                chid = cur.fetchone()[0]
                                print(chid, user_id, norm)
                                result = requests.get(f"https://www.googleapis.com/youtube/v3/search?key={oafs[norm]['key']}&channelId={chid}&part=snippet&order=date&maxResults=20")
                                r = result.json()['items']
                                utc = pytz.utc
                                now = datetime.utcnow().replace(tzinfo=utc)
                                for ip, post in enumerate(r):
                                    if ip != len(r) - 1:
                                        cur.execute("""INSERT INTO users_oauthpost (created, service, pdj, user_id) VALUES (%s, %s, %s, %s);""", (now, norm, json.dumps(post), user_id))
                                        # conn.commit()
                                    else: ## if last post
                                        cur.execute("""INSERT INTO users_oauthpost (created, service, pdj, user_id) VALUES (%s, %s, %s, %s);""", (now, norm, json.dumps(post), user_id))
                                        # conn.commit()
                                        cur.execute("""SELECT * FROM users_globalspflid;""")
                                        spfl_id = cur.fetchall()
                                        if len(spfl_id) == 0:
                                            cur.execute("""INSERT INTO users_globalspflid VALUES (1, '{}');""")
                                            # conn.commit()
                                        cur.execute("""SELECT id FROM users_oauthpost WHERE user_id = %s AND service = %s ORDER BY id DESC LIMIT 1;""", (user_id, norm))
                                        fspfl_id = f"{ { cur.fetchone()[0] } }"
                                        cur.execute("""UPDATE users_globalspflid SET spfl_id = array_cat(spfl_id, %s);""", (fspfl_id,)) #"{ 69 }"
                                        # conn.commit()
                        else:
                            print('This service is not yet supported for API Integration.')
                    else:
                        print('Share SPF disabled')
                    print('</account>')
        print('----------------')
except SyntaxError:
    print("UNABLE TO CONNECTT!tt!t!~~~~~~")

#!/usr/bin/env python3

import requests
import redis
import json
from summa import keywords

uri = "https://www.eventbriteapi.com/v3/events/search?location.address=mississauga&location.within=100km&expand=venue"
r = requests.get(uri, headers={'Authorization': 'Bearer FFXHJQX35Z4BHTSHXFVD'})
rd = redis.StrictRedis(host='plan_redis', port=6379, db=0, decode_responses=True)

#pprint.pprint(r.json())

# for key in r.json()["events"]:
#     print(key["id"])

cat_list = {
    '101': "business-professional",
    '102': "science-technology",
    '103': "music",
    '104': "film-media",
    '105': "arts",
    '106': "fashion-beauty",
    '107': "health-wellness",
    '108': "sports-fitness",
    '109': "travel-outdoor",
    '110': "food-drink",
    '111': "charity-causes",
    '112': "government-politics",
    '113': "community-culture",
    '114': "religion-spirituality",
    '115': "family-education",
    '116': "seasonal-holiday",
    '117': "home-lifestyle",
    '118': "auto-boat-air",
    '119': "hobbies-special-interest",
    '120': "school-activities",
    '199': "other"
}

def id_to_c(cat_id, desc):
    if not cat_id:
        cat_id = '119'
    memes = keywords.keywords(str(desc)).split()
    lmaos = [cat_list[cat_id]]
    return lmaos + memes


c = {"events": []}

json_events = r.json()["events"]
events_id = {event["id"]: event for event in json_events}.values() 
events = {f'{event["venue"]["address"]}{event["start"]["utc"]}': event for event in events_id}.values() 
# print(type(json_events), 'MEMEMEMES')
# events = []

# for current_event, next_event in zip(json_events, json_events[1:]):
#     if not current_event["id"] == next_event["id"] and not (current_event["venue"]["address"] == next_event["venue"]["address"] and current_event["start"]["utc"] == next_event["start"]["utc"]):
#         events.append(current_event)

# for i, e in enumerate(json_events):
    # for i_d, ed in enumerate(json_events):
    #     if not i == i_d:
    #         if e["id"] == ed["id"] or (e["venue"]["address"] == ed["venue"]["address"] and e["start"]["utc"] == ed["start"]["utc"]):
    #             pass
    #         else:
    #             events.append(e)

# print(events)
    
for e in events:
    ### grab keywords from e["description"]
    # print(e)
    # print('``````')
    image = ''
    start = ''
    location = ''
    if e["logo"]:
        image = e["logo"]["url"]
    if e["start"]:
        start = e["start"]["utc"]
    if e["venue"]:
        if e["venue"]["address"]["address_1"] and e["venue"]["address"]["localized_area_display"]:
            location = e["venue"]["address"]["address_1"] + ', ' + e["venue"]["address"]["localized_area_display"]
        elif e["venue"]["address"]["address_1"]:
            location = e["venue"]["address"]["address_1"]
        elif e["venue"]["address"]["localized_area_display"]:
            location = e["venue"]["address"]["localized_area_display"]
    c["events"].append({
        "id": e["id"],
        "image": image,
        "name": e["name"],
        "url": e["url"],
        "start": start,
        "location": location,
        "category": id_to_c(e["category_id"], e["description"]["text"])
    })
#     for key in 

# e = r.json()["events"][0]
# print(r.json()["events"][0]["id", "format", "name", "description"])

# print('this is C: ', c)

rd.set('brampton', json.dumps(c))

# d = json.loads(rd.get('brampton'))

# print('this is D: ', d)
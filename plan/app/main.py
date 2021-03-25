from starlette.applications import Starlette
from starlette.responses import JSONResponse
import redis
from random import shuffle
import json

r = redis.StrictRedis(host='plan_redis', port=6379, db=0, decode_responses=True)

api = Starlette()


@api.route("/all", methods=['POST'])
async def homepage(request):
    events = []
    j = await request.json()
    it = j["it"]
    if it[0] == 'all':
        d = json.loads(r.get('brampton'))
        events.append(d["events"][:10])
    else:
        do = json.loads(r.get('brampton'))
        for event in do["events"]:
            cl = event["category"] #if type(do["events"][i]["category"]) is list else [do["events"][i]["category"]]
            # if type(cl) is not list:
            #     cl = [cl] #
            # events.append([i for i in it if i in cl])
            # for sit in it:
            #     matching = len([s for s in cl if sit in s])
            # if any(elem in it for elem2.find(elem) in cl):
                # events.append(do["events"][i])
            # print(cl)
            for elem in it:
                for elem2 in cl:
                    if elem in elem2 or elem2 in elem:
                        events.append(event)


    # cached_data = json.loads(r.get('brampton'))

    # foo = r.get('foo')
    # if not foo:
    #     r.set('foo', 'bar')
    shuffle(events)
    return JSONResponse({"message": events[:10]})
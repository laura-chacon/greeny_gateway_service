import falcon, requests
import json

class GetActionHistoryController(object):
    def on_get(self, req, resp, uid):
        print 2222
        r = requests.get(
            "http://127.0.0.1:8002/users/"+ str(uid) + "/validate_token",
            headers={"Content-Type": "application/json",
                     "Accept": "application/json",
                     "Token": req.get_header('Token')}
        )
        if r.status_code == requests.codes.ok:
            r = requests.get(
                "http://127.0.0.1:8001/users/" + uid + "/history",
                data=json.dumps({}),
                headers={"Content-Type": "application/json",
                         "Accept": "application/json"},
            )
            body = json.loads(r.content)
            req.context['result'] = body
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_401

import falcon, requests, json

class CreateActionController(object):
    def on_put(self, req, resp, uid, action_id):
        r = requests.get(
            "http://127.0.0.1:8002/users/"+ str(uid) + "/validate_token",
            headers={"Content-Type": "application/json",
                     "Accept": "application/json",
                     "Token": req.get_header('Token')}
        )
        if r.status_code == requests.codes.ok:
            r = requests.put(
                "http://127.0.0.1:8001/users/"+ str(uid) + "/actions/" + str(action_id),
                data=json.dumps(req.context['body']),
                headers={"Content-Type": "application/json",
                         "Accept": "application/json"}
            )
            body = json.loads(r.content)
            req.context['result'] = body
            resp.status = falcon.HTTP_200
        else:
            req.context['result'] = {}
            resp.status = falcon.HTTP_401

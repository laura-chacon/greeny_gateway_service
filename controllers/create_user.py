import falcon, requests, json

class create_user(object):
    def on_put(self, req, resp, uid):
        r = requests.put(
            "http://127.0.0.1:8001/users/" + str(uid),
            data=json.dumps(req.context['body']),
            headers={"Content-Type": "application/json",
                     "Accept": "application/json"}
        )
        token = json.loads(r.content)['token']
        req.context['result'] = {'token': token}
        resp.status = falcon.HTTP_200

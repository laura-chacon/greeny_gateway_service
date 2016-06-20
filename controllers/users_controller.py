import falcon, requests
import json

class UsersController(object):
    def on_get(self, req, resp):
        payload = {'email': req.get_param('email')}
        r = requests.get(
            "http://127.0.0.1:8001/users",
            params=payload,
            headers={"Content-Type": "application/json",
                     "Accept": "application/json"},
        )
        body = json.loads(r.content)
        req.context['result'] = body
        resp.status = falcon.HTTP_200

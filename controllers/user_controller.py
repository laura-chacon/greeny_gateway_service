import falcon, requests
import json

class UserController(object):
    def on_put(self, req, resp, uid):
        request_body = {
            'email': req.context['body'].get('email'),
            'password': req.context['body'].get('password')
        }
        r = requests.put(
            "http://127.0.0.1:8001/users/" + str(uid),
            data=json.dumps(request_body),
            headers={"Content-Type": "application/json",
                     "Accept": "application/json"}
        )
        body = json.loads(r.content)
        req.context['result'] = body
        resp.status = falcon.HTTP_200

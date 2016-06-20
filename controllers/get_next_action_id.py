import falcon, requests
import json

class GetNextActionIdController(object):
    def on_get(self, req, resp, uid):
        r = requests.get(
            "http://127.0.0.1:8001/users/" + uid + "/actions/next_id",
            data=json.dumps({}),
            headers={"Content-Type": "application/json",
                     "Accept": "application/json"},
            decode='utf-8',
            body="")
        body = json.loads(r.content)
        req.context['result'] = body
        resp.status = falcon.HTTP_200

import falcon, requests
import json

class FactsController(object):
    def on_get(self, req, resp):
        r = requests.get(
            "http://127.0.0.1:8003/facts",
            headers={"Content-Type": "application/json",
                     "Accept": "application/json"}
        )
        body = json.loads(r.content)
        req.context['result'] = body
        resp.status = falcon.HTTP_200

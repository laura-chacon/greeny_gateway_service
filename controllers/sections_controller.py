import falcon, requests
import json

class SectionsController(object):
    def on_get(self, req, resp):
        r = requests.get(
            "http://127.0.0.1:8004/sections",
            headers={"Content-Type": "application/json",
                     "Accept": "application/json"}
        )
        body = json.loads(r.content)
        req.context['result'] = body
        resp.status = falcon.HTTP_200

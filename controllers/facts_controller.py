import falcon

class FactsController(object):
    def on_get(self, req, resp):
        r = requests.get(
            "http://127.0.0.1:8003/facts",
            data=json.dumps({}),
            headers={"Content-Type": "application/json",
                     "Accept": "application/json"},
            decode='utf-8',
            body=""
        )
        body = json.loads(r.content)
        req.context['result'] = body
        resp.status = falcon.HTTP_200

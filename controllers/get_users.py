import falcon, requests, json

class get_users(object):
    def on_get(self, req, resp):
        payload = {'email': req.get_param('email')}
        r = requests.get(
            "http://127.0.0.1:8001/users", 
            params = payload
        )
        resp.body = r.content['result']
        resp.status = falcon.HTTP_200

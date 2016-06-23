import falcon, requests, json

class ValidatePassword(object):
    def on_post(self, req, resp, uid):
        r = requests.post(
            "http://127.0.0.1:8002/users/" + str(uid) + "/validate_password",
            data=json.dumps(req.context['body']),
            headers={"Content-Type": "application/json",
                     "Accept": "application/json"}
        )
        req.context['result'] = r.content
        field_name = "HTTP_" + str(r.status_code)
        resp.status = getattr(falcon, field_name)

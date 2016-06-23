import falcon
import json

class ValidateToken(object):
    def on_get(self, req, resp, uid):
        token = req.get_header('Token')
        r = requests.get(
                "http://127.0.0.1:8002/users/"+ str(uid) + "/validate_token",
            data=json.dumps(req.context['body']),
            headers={"Content-Type": "application/json",
                     "Accept": "application/json",
                     "Token": token}
            )
        field_name = "HTTP_" + str(r.status_code)
        resp.status = getattr(falcon, field_name)      

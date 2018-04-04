execfile("./utilities.py")

import urllib2

# Router Class
class Router():
    api_url_str = "https://splife-emp-production.herokuapp.com/public/api/v1"
    method = HttpMethods.GET
    action = Action.READ
    competition_id = "0"
    def __init__(self, action, competition_id, token, data = None, participation_id = None):
        self.token = token
        self.action = action
        self.competition_id = competition_id
        self.data = data
        self.participation_id = participation_id
    def url(self):
        base_string = self.api_url_str + "/competitions/" + str(self.competition_id) + "/participations"
        if self.participation_id == None:
            return base_string
        else:
            return base_string + "/" + str(self.participation_id)
    def method(self):
        return self.action
    def request(self):
        headers = {
            'Authorization': 'Bearer ' + self.token,
            'Content-Type': 'application/json'
        }
        request =  urllib2.Request(self.url(), data=self.data, headers=headers)
        if Action.DELETE == self.action:
            request.get_method = lambda: 'DELETE'
        elif Action.CREATE == self.action:
            request.get_method = lambda: 'POST'
        elif Action.UPDATE == self.action:
            request.get_method = lambda: 'PATCH'
        return request

execfile("./utilities.py")
execfile("./sample_participation.py")
execfile("./router.py")

import urllib2

# CRUD class
class ParticipationCrudExampleCase():
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    participation = SampleParticipation()
    def __init__(self, competition_id, api_key, team = False):
        self.competition_id = competition_id
        self.api_key = api_key
        self.team = team
        if team:
            self.participation.team_name = "Team Splife"
    def run(self):
        try:
            print "Running CRUD"
            self.list_participations()
            self.create_participation()
            self.list_participations()
            self.update_participation()
            self.list_participations()
            self.delete_participation()
            self.list_participations()
            print "CRUD has been demonstrated, and side effects should be cleaned up"
        except urllib2.HTTPError as error:
            print "HTTPError "
            print "Code: ", error.code
            print "Body: ", error.read()
            if error.code == 401:
                print "You have a token/competition_id/permission issue"
            else:
                print "You have an unhandled error please open a github issue"
            pass

    def update_participation(self):
        participation = self.participation
        participation.first_name = "Mario"
        participation.last_name = "Lacerda"
        data = participation.to_json()
        req = Router(Action.UPDATE, self.competition_id, self.api_key, data, participation.id).request()
        response = self.opener.open(req)
        json_string = response.read()
        self.participation = SampleParticipation.decodeFromJson(json_string)
        print "Updated Participation: ", self.participation
    def create_participation(self):
        data = self.participation.to_json()
        req = Router(Action.CREATE, self.competition_id, self.api_key, data).request()
        response = self.opener.open(req)
        json_string = response.read()
        self.participation = SampleParticipation.decodeFromJson(json_string)
        print "Created Participation: ", self.participation
    def list_participations(self):
        req = Router(Action.READ, self.competition_id, self.api_key).request()
        response = self.opener.open(req)
        json_string = response.read()
        decoded = SampleParticipation.decodeFromJson(json_string)
        print "Participation List From The API: ", decoded
    def delete_participation(self):
        if self.participation != None:
            req = Router(Action.DELETE, self.competition_id, self.api_key, participation_id = self.participation.id).request()
            response = self.opener.open(req)
            json_string = response.read()
            print "Delete Response " + json_string
        else:
            print "No Participation set, can't delete"


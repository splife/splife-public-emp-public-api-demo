execfile("./utilities.py")
import json

# Sample Data Class
class SampleParticipation():
    def __init__(self, json_dict = None):
        if json_dict == None:
            self.id = None
            self.first_name = "Shaun"
            self.last_name = "Hubbard"
            self.email = "shaun@example.com"
            self.birthday = "1984-09-10T17:09:00+00:00"
            self.bib = "My Bib"
            self.gender = "m"
            self.team_bib = None
        else:
            self.__dict__ = json_dict
    def to_json(self):
        return json.dumps(self.__dict__)
    @staticmethod
    def decodeFromJson(json_string):
        json_obj = json.loads(json_string)
        if isinstance(json_obj, list):
            return list(map(lambda json_dict: SampleParticipation(json_dict), json_obj))
        elif isinstance(json_obj, dict):
            return SampleParticipation(json_obj)
        else:
            raise ValueError("Unknown json object")
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        string = "SampleParticipation: \n{\n"
        for key, val in self.__dict__.iteritems():
            string += "  \'" + str(key) + "\': " + str(val) + ",\n"
        string += "}"
        return string

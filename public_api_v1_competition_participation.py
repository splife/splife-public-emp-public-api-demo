#!/usr/bin/env python

# Script Developed in Python 2.7
# Maintainer:
#    Shaun Hubbard
#    contact: Shaun@splife.com
#    Developed for Splife, LLC

execfile("./utilities.py")
execfile("./participation_crud.py")


# Script Run
print "Splife EMP Public API V1 Participation Management Script"
console_offset()
# User Input
api_token = raw_input("Please enter your API Token: ")
solo_competition_id = raw_input("Please enter the solo competition id you wish to test(leave blank if none): ")
team_competition_id = raw_input("Please enter the team competition id you wish to test(leave blank if none): ")

solo_competition_id = maybe_parse_int(solo_competition_id)
team_competition_id = maybe_parse_int(team_competition_id)

# Automation
if solo_competition_id != None:
    ParticipationCrudExampleCase(solo_competition_id, api_token).run()

if team_competition_id != None:
    ParticipationCrudExampleCase(team_competition_id, api_token, True).run()


# Print success statement
print "Script run successful!"
exit(0)

from conf.Config import Config
from Action import Action

class Profile:

    _actions = []

    def __init__(self ):
        print ('Profile Constructor')
    
    def initialize(self, a_iIndex, refBoard):
        print ('Profile Initialization. Active Profile Index: '  + str(a_iIndex))
        profileData = Config.getInstance().getProfile(a_iIndex)
        if(profileData is False):
            print ('Could not get the profile data from configuration!')
            return False
        actionsData = profileData['actions']
        for actionData in actionsData:
            action = Action()
            action.initialize(actionData)
            refBoard.attach(action)
            self._actions.append(action)
        return True

    def cleanUP(self, refBoard):
        print ('Perform any clean up here')
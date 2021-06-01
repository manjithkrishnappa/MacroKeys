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
        # print ('Profile Data:' + str(profileData))
        actionsData = profileData['actions']
        for actionData in actionsData:
            #print ('Action Data:' + str(actionData))
            action = Action()
            action.initialize(actionData)
            refBoard.attach(action)
            self._actions.append(action)
        return True

    def cleanUP(self, refBoard):
        # for act in self._actions:
        #     refBoard.detach(act)
        print ('Perform any clean up here')
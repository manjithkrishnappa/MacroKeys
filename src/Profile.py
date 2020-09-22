from conf.Config import Config

class Profile:

    def __init__(self ):
        print ('Profile Constructor')
    
    def initialize(self, a_iIndex):
        print ('Profile Initialization. Active Profile Index: '  + str(a_iIndex))
        profileData = Config.getInstance().getProfile(a_iIndex)
        if(profileData is False):
            print ('Could not get the profile data from configuration!')
            return False
        # print ('Profile Data:' + str(profileData))
        actions = profileData['actions']
        for action in actions:
            print ('Action Data:' + str(action))
        return True
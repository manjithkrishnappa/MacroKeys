import json
import os.path
from os import path

class Config:
    #private member variables
    _fileName = 'MacroKeys.conf'
    _filePath = '/etc/MacroKeys/'
    _fileNameWithPath = _filePath + _fileName

    _keyboardName = ''
    _profiles=[]

    _isInitialized = False

    __instance = None
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if Config.__instance == None:
            Config()
        return Config.__instance

    def __init__(self):
        print ("Config Constructor")
        """ Virtually private constructor. """
        if Config.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Config.__instance = self
        
    def initialize(self):
        print ("Initilizing Config")
        if(self._checkElseCreateConfFile() is not True):
            return False
        if(self._readConfFile() is not True):
            return False
        self._isInitialized = True
        return True
    
    def _checkElseCreateConfFile(self):
        #check if the directory exists else create the directory
        if not path.isdir(self._filePath):
            try:
                print ('Directory does not Exist! Creating...')
                os.makedirs(self._filePath)
            except:
                print ('Could not create directory for config file')
                return False
        if not path.isfile(self._fileNameWithPath):
            print ('Conf file does not Exist! Creating...')
            if (self._createDefaultConf() is not True):
                return False
        return True
    
    def _createDefaultConf(self):
        data = {}
        data['keyboard_name'] = "board1"
        data['profiles'] = []
        try:
            with open(self._fileNameWithPath, 'w') as outfile:
                json.dump(data, outfile)
        except:
            print ('Could not create default config file')
            return False
        return True
    
    def _readConfFile(self):
        try:
            print (self._fileNameWithPath)
            with open(self._fileNameWithPath) as json_file:
                data = json.load(json_file)
            self._keyboardName = data['keyboard_name']
            self._profiles = data['profiles']
            # actions = self._profiles[0]['actions']
            # print(self._keyboardName)
            # print(actions[0])
            return True
        except Exception as e:
            print ('could not open / read the config file: ')
            print (e)
            return False
    
    def getProfile(self, a_iIndex):
        if(self._isInitialized is False):
            print ('Configuation has not been initialized yet')
            return False
        if(len(self._profiles) < a_iIndex):
            print (f'Trying to get {a_iIndex} profile. Total Available profiles {len(self._profiles)}')
            return False
        return self._profiles[a_iIndex]

    #Getter function for Keyboard Name
    def get_keyboardName(self):
        return self._keyboardName
    
    keyboardName = property (get_keyboardName)
        
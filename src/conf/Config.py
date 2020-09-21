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

    def __init__(self):
        print ("Config Constructor")
        
    def initialize(self):
        print ("Initilizing Config")
        self._checkElseCreateConfFile()
        self._readConfFile()
        return True
    
    def _checkElseCreateConfFile(self):
        #check if the directory exists else create the directory
        if not path.isdir(self._filePath):
            print ('Directory does not Exist! Creating...')
            os.makedirs(self._filePath)
        if not path.isfile(self._fileNameWithPath):
            print ('Conf file does not Exist! Creating...')
            self._createDefaultConf()
        return True
    
    def _createDefaultConf(self):
        data = {}
        data['keyboard_name'] = "board1"
        data['profiles'] = []
        with open(self._fileNameWithPath, 'w') as outfile:
            json.dump(data, outfile)
    
    def _readConfFile(self):
        try:
            print (self._fileNameWithPath)
            with open(self._fileNameWithPath) as json_file:
                data = json.load(json_file)
            _keyboardName = data['keyboard_name']
            _profiles = data['profiles']
            actions = _profiles[0]['actions']
            print(_keyboardName)
            print(actions[0])
            return True
        except Exception as e:
            print ('could not open / read the config file: ')
            print (e)
            return False
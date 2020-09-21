import json
import os.path
from os import path

class Config:
    #private member variables
    _fileName = 'MacroKeys.conf'
    _filePath = '/home/mkrishnappa/Work/Projects/MacroKeys/MacroKeys/src/conf/'
    _fileNameWithPath = _filePath + _fileName

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
        #TODO: Create a better default fie.
        data['width'] = 932
        data['height'] = 865
        with open(self._fileNameWithPath, 'w') as outfile:
            json.dump(data, outfile)
    
    def _readConfFile(self):
        try:
            print (self._fileNameWithPath)
            with open(self._fileNameWithPath) as json_file:
                data = json.load(json_file)
            width = data['width']
            height = data['height']
            print(width)
            print(height)
            return True
        except:
            print ('could not open / read the config file')
            return False
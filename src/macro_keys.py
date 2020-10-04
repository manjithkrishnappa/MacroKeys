#!/usr/bin/env python

import time
from conf.Config import Config
from board.Board import Board
from configurator.Configurator import Configurator
from Profile import Profile
import gi
import threading
import sys
# from pathlib import Path

class Main:
  #TODO: This should come from a save file
  _activeProfileIndex = 0
  _isInitialized = False

  def initialize(self):
    try:
      if(Config.getInstance().initialize() is False):
        return False
      if(self.board.initialize() is False):
        return False
      if(self.activeProfile.initialize(self._activeProfileIndex, self.board) is False):
        return False
      if(self._configurator.Initialize() is False):
        return False
      _isInitialized = True
      return True
    except Exception as exp:
      print ('Initialization Failed')
      print (exp)
      return False

  def cleanUp(self):
      print("Clean Up called!")
      self.board.cleanUp()
      #self._configurator.cleanUp()

  def parseArguments(self):
    if len(sys.argv) == 0:
      print ('No Arguments Passed!')
      return
    for arg in sys.argv:
      print (f'Argument: {arg}')


  def __init__(self):
    #Create Obejects of other classes
    Config.getInstance()
    self.board = Board()
    self.activeProfile = Profile()
    self._configurator = Configurator()

    if(self.initialize() is False):
      print ('Could not initialize; Exiting!')
      return

    boardThread = threading.Thread(target= self.board.run)
    boardThread.start()
    
    self._configurator.runGTK_Main()

if __name__ == "__main__":
    main = Main()
    
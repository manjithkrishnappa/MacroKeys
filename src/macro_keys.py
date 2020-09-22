#!/usr/bin/env python

import time
from conf.Config import Config
from board.Board import Board
from Profile import Profile

class Main:
  #TODO: This should come from a save file
  _activeProfileIndex = 0

  def initialize(self):
    try:
      if(Config.getInstance().initialize() is False):
        return False
      if(self.activeProfile.initialize(self._activeProfileIndex) is False):
        return False
      if(self.board.initialize() is False):
        return False
      return True
    except:
      print ('Initialization Failed')
      return False

  def cleanUp(self):
      print("Clean Up called!")
      self.board.cleanUp()

  def __init__(self):
    #Create Obejects of other classes
    Config.getInstance()
    self.board = Board()
    self.activeProfile = Profile()

    if(self.initialize() is False):
      print ('Could not initialize; Exiting!')
      return
    #This will make the operation run in a loop and keep polling for input on the board
    self.board.run()

    time.sleep(0.01)
    self.cleanUp()
    print("Exit!")

if __name__ == "__main__":
    main = Main()
#!/usr/bin/env python

import time
from Action import Observer
from conf.Config import Config
from board.Board import Board
from configurator.Configurator import Configurator
from Profile import Profile
import gi
import threading
import sys
# from pathlib import Path

class Main(Observer):
  _isInitialized = False

  #TODO: This should come from a save file
  _activeProfileIndex = 0

  #Variables that can be overriden by passing arguments to the class
  _argShowUI = False

  def initialize(self):
    try:
      if(Config.getInstance().initialize() is False):
        return False
      if(self.board.initialize() is False):
        return False
      if(self.activeProfile.initialize(self._activeProfileIndex, self.board) is False):
        return False
      # if(self._configurator.Initialize(self._argShowUI) is False):
      #   return False
      _isInitialized = True
      return True
    except Exception as exp:
      print ('Initialization Failed')
      print (exp)
      return False

  def cleanUp(self):
      print("Clean Up called!")
      self.activeProfile.cleanUP(self.board)
      # self._configurator.cleanUp()
      self.board.cleanUp()

  def parseArguments(self):
    if len(sys.argv) == 0:
      print ('No Arguments Passed!')
      return
    # for arg in sys.argv:
    #   print (f'Argument: {arg}')
    if('-h' or '--help' in sys.argv):
      print ('HELP MENU')
    if('showui' in sys.argv):
      print ('Show UI is passed as an arg')
      self._argShowUI = True
    

  def __init__(self):

    self.parseArguments()

    #Create Obejects of other classes
    Config.getInstance()
    self.board = Board()
    self.activeProfile = Profile()
    # self._configurator = Configurator()

    if(self.initialize() is False):
      print ('Could not initialize; Exiting!')
      return

    self._boardThread = threading.Thread(target= self.board.run)
    self._boardThread.start()
    
    # self._configurator.runGTK_Main()

    self.board.attachEndObserver(self)
    pass

  def update(self, arg):
    print ('Cleaning up and exiting!')
    self.cleanUp()

if __name__ == "__main__":
    main = Main()
    
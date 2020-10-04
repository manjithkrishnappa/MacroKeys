#!/usr/bin/env python

import time
from conf.Config import Config
from board.Board import Board
from configurator.Configurator import Configurator
from Profile import Profile
import gi
import threading
# from pathlib import Path
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk

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
      self.cleanUp()
      return False

  def cleanUp(self):
      print("Clean Up called!")
      self.board.cleanUp()
      #self._configurator.cleanUp()

  def __init__(self):
    #Create Obejects of other classes
    Config.getInstance()
    self.board = Board()
    self.activeProfile = Profile()
    self._configurator = Configurator()

    if(self.initialize() is False):
      print ('Could not initialize; Exiting!')
      return

    # if(self.InitializeUI() is False):
    #   print ('Could not initialize UI; Exiting!')
    #   return

    boardThread = threading.Thread(target= self.board.run)
    boardThread.start()

if __name__ == "__main__":
    main = Main()
    gtk.main()
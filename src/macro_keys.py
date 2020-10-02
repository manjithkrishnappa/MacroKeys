#!/usr/bin/env python

import time
from conf.Config import Config
from board.Board import Board
from Profile import Profile
import gi
import threading
import os
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
      _isInitialized = True
      return True
    except:
      print ('Initialization Failed')
      return False

  def cleanUp(self):
      print("Clean Up called!")
      self.board.cleanUp()
  
  def InitializeUI(self):
    #TODO: The application should be a system tray app
    absPathGladeFile = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
    absPathGladeFile = os.path.join(absPathGladeFile, '../ui/MacroKeys_Configurator.glade')
    print (f'Absolute path to the Glade file is {1}', absPathGladeFile)
    gladeFile = './ui/MacroKeys_Configurator.glade'
    self.builder = gtk.Builder()
    self.builder.add_from_file(absPathGladeFile)

    window = self.builder.get_object("main")
    window.connect("destroy", self.cleanUpUI)
    window.show()
    print ("Should be showing the window now")
    
    return True
  
  def cleanUpUI(self, widget):
    self.cleanUp()
    print("Exit!")
    gtk.main_quit(widget)


  def __init__(self):
    #Create Obejects of other classes
    Config.getInstance()
    self.board = Board()
    self.activeProfile = Profile()

    if(self.initialize() is False):
      print ('Could not initialize; Exiting!')
      return

    if(self.InitializeUI() is False):
      print ('Could not initialize UI; Exiting!')
      return

    boardThread = threading.Thread(target= self.board.run)
    boardThread.start()

if __name__ == "__main__":
    main = Main()
    gtk.main()
#!/usr/bin/env python

import time
from conf.Config import Config
from board.Board import Board
from Profile import Profile
import gi
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
    gladeFile = './ui/MacroKeys_Configurator.glade'
    self.builder = gtk.Builder()
    self.builder.add_from_file(gladeFile)

    window = self.builder.get_object("main")
    #window.connect("delete-event", self.cleanUpUI)
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

    #This will make the operation run in a loop and keep polling for input on the board
    #TODO: this should run in its own thread.
    self.board.run()

if __name__ == "__main__":
    main = Main()
    gtk.main()
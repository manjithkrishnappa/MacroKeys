#!/usr/bin/env python

import time
from conf.Config import Config
from board.Board import Board

class Main:

  def initialize(self):
    try:
      if(self.conf.initialize() is not True):
        return false
      if(self.board.initialize() is not True):
        return false
      return True
    except:
      print ('Initialization Failed')
      return False

  def cleanUp(self):
      print("Clean Up called!")
      self.board.cleanUp()

  def __init__(self):
    #Create Obejects of other classes
    self.board = Board()
    self.conf = Config()

    if(self.initialize() is not True):
      print ('Could not initialize; Exiting!')
      return
    #This will make the operation run in a loop and keep polling for input on the board
    self.board.run()

    time.sleep(0.01)
    self.cleanUp()
    print("Exit!")

if __name__ == "__main__":
    main = Main()
#!/usr/bin/env python
import subprocess
import time
import os
from evdev import InputDevice, categorize, ecodes



class Main:

  def OpenSlack(self):
    os.system('xdotool key Super')
    time.sleep(1)
    os.system('xdotool type "slack"')
    time.sleep(1)
    os.system('xdotool key Return')

  def OpenBlueJeans(self):
    os.system('xdotool key Super')
    time.sleep(1)
    os.system('xdotool type "bluejeans"')
    time.sleep(1)
    os.system('xdotool key Return')

  def SetUpWW(self):
    cmdSetupScript = 'sh /home/mkrishnappa/Work/WFS/set_up_workspace/setup_ww_develop.sh'
    proc1=subprocess.Popen(cmdSetupScript, shell=True, stdout=subprocess.PIPE)
    proc1.communicate()[0]
    #boardEvent = boardEvent.decode('UTF-8').rstrip('\n')

  def initialize(self):
    print('Starting the macro service')
    self.dev.grab()

  def run(self):
    for event in self.dev.read_loop():
      if event.type == ecodes.EV_KEY:
        key = categorize(event)
        if key.keystate == key.key_down:
          print (key.keycode)
          if key.keycode == 'KEY_KPENTER':
            print ('Going to break out of the loop')
            break
          if key.keycode == 'KEY_KP0':
            os.system('xdotool key Super;')
            os.system('xdotool type "steam"; xdotool key Return')
          if key.keycode == 'KEY_KP1':
            OpenSlack()
          if key.keycode == 'KEY_KP2':
            OpenBlueJeans()

  def cleanUp(self):
      print("Clean Up called!")
      self.dev.ungrab()

  def __init__(self):
    #TODO: Put this in a function and use try catch blocks and handle the errors
    cmdFindBoardEvent = 'grep -A 5 -w \'"SEM USB Keyboard"\' /proc/bus/input/devices |grep sysrq |awk \'{print $4}\''
    proc=subprocess.Popen(cmdFindBoardEvent, shell=True, stdout=subprocess.PIPE)
    boardEvent = proc.communicate()[0]
    boardEvent = boardEvent.decode('UTF-8').rstrip('\n')
    boardEventFullPath = '/dev/input/'  + boardEvent
    print (boardEventFullPath)
    self.dev = InputDevice(boardEventFullPath)

    self.initialize()
    self.run()
    time.sleep(0.01)
    self.cleanUp()
    print("Exit!")

if __name__ == "__main__":
    main = Main()
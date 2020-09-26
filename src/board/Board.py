import subprocess
import time
import os
from evdev import InputDevice, categorize, ecodes

class Board:
    def __init__(self):
        print ("Board Constructor")
        self._observers = set()
        #self._key

    def initialize(self):
        try:
            cmdFindBoardEvent = 'grep -A 5 -w \'"SEM USB Keyboard"\' /proc/bus/input/devices |grep sysrq |awk \'{print $4}\''
            proc=subprocess.Popen(cmdFindBoardEvent, shell=True, stdout=subprocess.PIPE)
            boardEvent = proc.communicate()[0]
            boardEvent = boardEvent.decode('UTF-8').rstrip('\n')
            boardEventFullPath = '/dev/input/'  + boardEvent
            print (boardEventFullPath)
            self.dev = InputDevice(boardEventFullPath)
            print('Starting the macro service')
            self.dev.grab()
            return True
        except:
            print ('Could not get the grab board')
            return False
    
    def run(self):
        for event in self.dev.read_loop():
            if event.type == ecodes.EV_KEY:
                self._key = categorize(event)
                self._notify()
                if self._key.keystate == self._key.key_down:
                    print (self._key.keycode)
                    if self._key.keycode == 'KEY_KPENTER':
                        print ('Going to break out of the loop')
                        break
                    if self._key.keycode == 'KEY_W':
                        self.SetUpWW()

    def cleanUp(self):
        self.dev.ungrab()

    #Obeserver Pattern Functions
    def attach(self, observer):
        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        observer._subject = None
        self._observers.discard(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update(self._key)

    def SetUpWW(self):
        cmdSetupScript = 'sh /home/mkrishnappa/Work/WFS/set_up_workspace/setup_ww_develop.sh'
        proc1=subprocess.Popen(cmdSetupScript, shell=True, stdout=subprocess.PIPE)
        proc1.communicate()[0]
    
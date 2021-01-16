import subprocess
import time
import os
from evdev import InputDevice, categorize, ecodes
from conf.Config import Config

class Board:
    _shouldRun = True
    # Use this flag to quickly turn off all functionality in the class while developing
    _shouldInitialize = True


    def __init__(self):
        print ("Board Constructor")
        self._observers = set()
        #self._key

    def initialize(self):
        if (self._shouldInitialize is False):
            return
        try:
            keyboardName = Config.getInstance().keyboardName
            cmdFindBoardEvent = 'grep -A 5 -w ' + keyboardName + ' /proc/bus/input/devices |grep sysrq |awk \'{print $4}\''
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
        if (self._shouldInitialize is False):
            return
        print ('Thread Run')
        for event in self.dev.read_loop():
            if( self._shouldRun is False):
                break
            if event.type == ecodes.EV_KEY:
                self._key = categorize(event)
                self._notify()
                if self._key.keystate == self._key.key_down:
                    print (self._key.keycode)
                    if self._key.keycode == 'KEY_KPENTER':
                        print ('Going to break out of the loop')
                        #TODO: If we keep this then we should let the main function know that the thread has stopped
                        self._shouldRun = False

    def cleanUp(self):
        if (self._shouldInitialize is False):
            return
        self._shouldRun = False
        self.dev.ungrab()

    #Obeserver Pattern Functions
    def attach(self, observer):
        if (self._shouldInitialize is False):
            return
        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        if (self._shouldInitialize is False):
            return
        observer._subject = None
        self._observers.discard(observer)

    def _notify(self):
        if (self._shouldInitialize is False):
            return
        for observer in self._observers:
            observer.update(self._key)    
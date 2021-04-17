import subprocess
import time
import os
import evdev
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
            devices = [InputDevice(path) for path in evdev.list_devices()]
            for device in devices:
                # print(device.path, device.name, device.phys)
                if device.name == Config.getInstance().keyboardName:
                    print('Keyboard Found:', device.name)
                    self.dev = device
                    self.dev.grab()
                    return True
            print ('Could not find the board: ' + Config.getInstance().keyboardName + '. Make sure the board is connected')
            return False
        except Exception as exp:
            print ('Could not get the grab board: ' + exp)
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
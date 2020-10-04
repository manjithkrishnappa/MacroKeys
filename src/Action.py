import abc
import time
import os

class Observer(metaclass=abc.ABCMeta):
    """
    Define an updating interface for objects that should be notified of
    changes in a subject.
    """

    def __init__(self):
        self._subject = None
        self._keyEvent = None

    @abc.abstractmethod
    def update(self, arg):
        pass

class Action(Observer):

    def __init__(self):
        # print ('Action Constructor')
        pass
    
    def initialize(self, a_Data):
        # print ('Action Initialization, Action Data: ' + str(a_Data))
        self._id = a_Data['id']
        self._name = a_Data['name']
        self._keyBind = a_Data['key_bind']
        self._keyType = a_Data['type'].strip()
        self._simulatedKeys = a_Data['keys']
        self._animSpeed = a_Data['anim_speed']
    
    def update(self, arg):
        self._keyEvent = arg
        # print (f'Update in the Action class with ID: {self._id}! Key Code: {self._keyEvent.keystate}')
        if self._keyEvent.keystate == self._keyEvent.key_down:
            if self._keyEvent.keycode == self._keyBind:
                # print (f'Action class {self._id} will be activated with {self._simulatedKeys}')
                self._perform()

    def _perform(self):
        if self._keyType == 'Key_Presses':
            self._performKeyPresses()


    def _performKeyPresses(self):
        for skey in self._simulatedKeys:
            # print (f'Keys to simulate: {skey}')
            if skey.startswith('\''):
                os.system('xdotool type ' + skey)
                time.sleep(self._animSpeed)
            else:
                os.system('xdotool key ' + skey)
                time.sleep(self._animSpeed)
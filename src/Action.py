import abc

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
        print ('Action Constructor')
    
    def initialize(self, a_Data):
        print ('Action Initialization, Action Data: ' + str(a_Data))
    
    def update(self, arg):
        self._observer_state = arg
        # ...
        print ('Update in the Action class!')
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
import os

#TODO: The application should be a system tray app
class Configurator:
    def __init__(self):
        print ("Hello Configurator")
        self.Initialize(True)
        self.runGTK_Main()

    def Initialize(self, showUI):
        self._showUI = showUI
        if(self._showUI is False):
            return

        absPathGladeFile = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
        absPathGladeFile = os.path.join(absPathGladeFile, '../../ui/MacroKeys_Configurator.glade')
        print (f'Absolute path to the Glade file is {1}', absPathGladeFile)
        gladeFile = './ui/MacroKeys_Configurator.glade'
        self.builder = gtk.Builder()
        self.builder.add_from_file(absPathGladeFile)

        window = self.builder.get_object("main")
        window.connect("destroy", self.cleanUp)
        window.show()
        print ("Should be showing the window now")

        self.ConnectSignals()

        return True
    
    def ConnectSignals(self):
        btnTryMe = self.builder.get_object("btnTryMe")
        btnTryMe.connect("released",self.hello)

    def runGTK_Main(self):
        if(self._showUI is False):
            return
        gtk.main()

    def cleanUp(self, widget):
        if(self._showUI is False):
            return
        #TODO: If we keep this then we should let the main function know that the thread has stopped
        gtk.main_quit(widget)

    def hello(self, button):
        print("hell, goodbye world!")

if __name__ == "__main__":
    main = Configurator()
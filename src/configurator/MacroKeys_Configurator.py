import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
from macro_keys import Main

###
# NOTE: This file is no longer in use
# The functionality of UI is moved to the macro_keys class
###


class cMain:
    def __init__(self):
        gladeFile = './ui/MacroKeys_Configurator.glade'
        self.builder = gtk.Builder()
        self.builder.add_from_file(gladeFile)

        window = self.builder.get_object("main")
        window.connect("delete-event", gtk.main_quit)
        window.connect("destroy", gtk.main_quit)
        window.show()

        Main()
    
if __name__ == "__main__":
    main = cMain()
    gtk.main()
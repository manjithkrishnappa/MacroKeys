import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk

class cMain:
    def __init__(self):
        gladeFile = './ui/MacroKeys_Configurator.glade'
        self.builder = gtk.Builder()
        self.builder.add_from_file(gladeFile)

        window = self.builder.get_object("main")
        window.connect("delete-event", gtk.main_quit)
        window.connect("destroy", gtk.main_quit)
        window.show()
    
if __name__ == "__main__":
    main = cMain()
    gtk.main()
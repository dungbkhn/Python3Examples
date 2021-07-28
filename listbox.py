import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, GObject
import sys

class Item(GObject.GObject):

    text = GObject.property(type = str)

    def __init__(self):
        GObject.GObject.__init__(self)

class GUI:

    def __init__(self):        
        item1 = Item()
        item1.text = "Hello"
        item2 = Item()
        item2.text = "World"

        liststore = Gio.ListStore()
        liststore.append(item1)
        liststore.append(item2)

        listbox=Gtk.ListBox()
        listbox.bind_model(liststore, self.create_widget_func)

        window = Gtk.Window()
        window.add(listbox)
        window.connect("destroy", self.on_window_destroy)
        window.show_all()

    def create_widget_func(self,item):
        label=Gtk.Label(item.text)
        return label

    def on_window_destroy(self, window):
        Gtk.main_quit()

def main():

    app = GUI()
    Gtk.main()

if __name__ == "__main__":
    sys.exit(main())

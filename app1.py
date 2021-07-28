import gi

gi.require_version("Gtk", "3.0")
gi.require_version('Notify', '0.7')

from gi.repository import Gtk as gtk
from gi.repository import Notify

class MyWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self, title="Hello World")
        gtk.Window.set_default_size(self, 640, 480)
        Notify.init("Simple GTK3 Application")

        self.box = gtk.Box(spacing=6)
        self.add(self.box)
       
        self.button = gtk.Button(label="Click Here")
        self.button.set_halign(gtk.Align.END)
        self.button.set_valign(gtk.Align.END)
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, True, True, 0)

    def on_button_clicked(self, widget):
        n = Notify.Notification.new("Simple GTK3 Application", "Hello World !!")
        n.show()

win = MyWindow()
win.connect("destroy", gtk.main_quit)
win.show_all()
gtk.main()

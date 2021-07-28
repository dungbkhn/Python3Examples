import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.ApplicationWindow):
    # a window

    def __init__(self, app):
        Gtk.Window.__init__(self, title="GNOME LinkButton", application=app)
        self.set_default_size(250, 50)

        # a linkbutton pointing to the given URI
        button = Gtk.LinkButton(uri="http://live.gnome.org")
        # with given text
        button.set_label("Link to GNOME live!")

        # add the button to the window
        self.add(button)


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)


win = MyApplication()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

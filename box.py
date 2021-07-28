import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)
        
        self.box1 = Gtk.Box(spacing=6)
        self.box2 = Gtk.Box(spacing=6)

        self.label1 = Gtk.Label(label="Hello")
        self.label1.set_halign(Gtk.Align.START)
        self.label1.set_valign(Gtk.Align.START)
        self.box1.pack_start(self.label1, False, False, 20)

        self.button2 = Gtk.Button(label="Button")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box2.pack_start(self.button2, False, False, 0)
        
        # a linkbutton pointing to the given URI
        self.button3 = Gtk.Label("ssdfds")
        button3.connect("clicked", self.on_button1_clicked)


        self.box2.pack_start(self.button3, False, False, 0)

        
        self.box.pack_start(self.box1,False,False,20)
        self.box.pack_start(self.box2,True,True,0)

    def on_button1_clicked(self, widget):
        print("Hello")

    def on_button2_clicked(self, widget):
        print("Goodbye")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

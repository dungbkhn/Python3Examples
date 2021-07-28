import gi
import os
import sys

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GridWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Grid Example")

        grid = Gtk.Grid()
        self.add(grid)

        self.button = Gtk.Button(label="Button 1")
        self.image = Gtk.Image()

        grid.add(self.button)
        grid.add(self.image)

        self.button.connect("clicked", self.load_image)

        self.count = 0
        
    def load_image(self, event):
       
        self.image.set_from_file("/home/dungnt/Pictures/a1.jpg")

        self.count = self.count + 1

win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

#!/usr/bin/python

import gi
gi.require_version("Gtk", "3.0")
gi.require_version('AppIndicator3', '0.1')
import os
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator

gi.require_version("Notify", "0.7")
from gi.repository import Notify

import subprocess

globalX = 0

class MyWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self, title="Hello World")
        gtk.Window.set_default_size(self, 640, 480)
        Notify.init("Simple GTK3 Application")
        self.icon = self.render_icon(gtk.STOCK_INDEX, 1)
        self.set_icon(self.icon)
        self.box = gtk.Box(spacing=6)
        self.add(self.box)
       
        self.button = gtk.Button(label="Click Here")
        self.button.set_halign(gtk.Align.END)
        self.button.set_valign(gtk.Align.END)
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, True, True, 0)

    def on_button_clicked(self, widget):
        #n = Notify.Notification.new("Simple GTK3 Application", "Hello World !!")
        #n.show()
        #win2 = MyWindow()
        #win2.connect("destroy", win)
        #win2.show_all()
        #os.system("cp /home/dungnt/SharedFolder/'Pi pc'/links.txt /home/dungnt")
        batcmd="cp /home/dungnt/SharedFolder/'Pi pc'/lindfgks.txt /home/dungnt"
        #x = subprocess.check_output(batcmd,shell=True)
        #messagebox.showinfo("showinfo", "Information")
        
    def on_delete_event(event, self, widget):
        globalX=0
        print(globalX)
        self.hide()
    #self.destroy_app()
        return True
	
def main():
  indicator = appindicator.Indicator.new("customtray", "semi-starred-symbolic", appindicator.IndicatorCategory.APPLICATION_STATUS)
  indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
  indicator.set_menu(menu())
  gtk.main()

def menu():
  menu = gtk.Menu()
  
  command_one = gtk.MenuItem(label="None", use_underline=False)
  command_one.connect('activate', note)
  menu.append(command_one)

  exittray = gtk.MenuItem(label="Exit", use_underline=True)
  exittray.connect('activate', quit)
  menu.append(exittray)
  
  menu.show_all()
  return menu
  
def note(_):
  #os.system("gedit $HOME/Documents/notes.txt")
  #notify()
  win = MyWindow()
  win.connect("delete-event", win.on_delete_event)
  win.show_all()
  globalX=1
  print(globalX)
def quit(_):
  gtk.main_quit()

if __name__ == "__main__":
  main()







	

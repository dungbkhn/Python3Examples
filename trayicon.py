#!/usr/bin/python

import gi
gi.require_version("Gtk", "3.0")
gi.require_version('AppIndicator3', '0.1')
import os
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator

gi.require_version("Notify", "0.7")
from gi.repository import Notify


# Init notifications
Notify.init("MyProgram")

def notify():
	# Create a new notification
	n = Notify.Notification.new("Default Title","Default Body")

	# Update the title / body
	n.update("Hello","World!")

	# Show it
	n.show()
	
	
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
  notify()
def quit(_):
  gtk.main_quit()

if __name__ == "__main__":
  main()







	

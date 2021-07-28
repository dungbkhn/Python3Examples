#!/usr/bin/python

import gi
gi.require_version("Gtk", "3.0")
gi.require_version('AppIndicator3', '0.1')
import os
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator, GLib as glib

gi.require_version("Notify", "0.7")
from gi.repository import Notify

import subprocess
import signal
import os
import time
import threading

def main():
  with open("/home/dungnt/hello.txt", "r") as file:
            first_line = file.readline()
            for last_line in file:
                pass
  print("lastline of hello.txt:"+last_line)
  if last_line=='go to sleep\n':
     print ('ok')
  


if __name__ == "__main__":
  main()



#!/usr/bin/env python

#Creates a shortcut that launches PiLib
import sys
import os
absdir = os.path.dirname(sys.argv[0])
absdir = absdir[0:-6]

fnm = "/PiLib.dekstop"
fpt = str(absdir)+fnm


shortcut = open(fpt, "w+")

shortcut.write("[Desktop Entry]\n")
shortcut.write("Name=Pi-Lib Shortcut\n")
shortcut.write("Comment=I launch Pi-Lib software\n")
shortcut.write("Icon=%s/MEDIA/icon.xpm\n" %(absdir))
shortcut.write("Exec=python %s/Pi-Lib.pyw\n" %(absdir))
shortcut.write("Type=Application\n")
shortcut.write("StartupNotify=false\n")

shortcut.close()

absdir = os.path.dirname(sys.argv[0])

autorunfnm="/autorun generator.desktop"
autoruncodefile="/autorun_creator.py"
autoruncodedir = absdir+autoruncodefile

autorunfpt = absdir+autorunfnm

autoruncfg = open(autorunfpt, "w+")
autoruncfg.write("[Desktop Entry]\n")
autoruncfg.write("Name=autorun generator\n")
autoruncfg.write("Comment=I launch the autorun creator\n")
autoruncfg.write("Icon=lxterminal\n")
autoruncfg.write("Exec=python %s\n" %(autoruncodedir))
autoruncfg.write("Type=Application\n")
autoruncfg.write("StartupNotify=false\n")

autoruncfg.close()

#!/usr/bin/env python

#Run this .py file in your PowerShell(windows) or Console (Linux), don't edit the code if you don't know what you're doing; it may (and most likely will) cause issues later on.
# single call op device.ini

######Importing dependencies
import platform
import time
import os
import subprocess
import sys
absdir = os.path.dirname(sys.argv[0])
fnm = "/device.ini"
fpt = str(absdir)+fnm

#print absdir



######FUNCTIONS
def wincheck():
    os.startfile(fpt)
    print "Close this program if you are happy with the settings in the configuration file."
    print "Rerun this program if you aren't happy with the settings in the configuration file."
    time.sleep(5)
    exit()

def unixcheck():
    prog = "leafpad"
    subprocess.Popen([prog, fpt])
    time.sleep(5)
    y = raw_input("Press <Enter> to close")
    exit()

#########Common sense msg:
print "These settings are used to identify the Pi computer, make sure you use unique name-description-location combinations."
print """A good example would be:
name = Bellerophon
description = raspberry pi with Raspbian.
location =  second floor near cabinet 5\n
A bad example would be:
name = Chimera
description = computer
location = indoors"""


#####Setting Variables
devicefile = open(fpt, "w+")
name = raw_input("Type the name of this device. ")
description = raw_input("Give a description of this device. ")
location = raw_input("Describe where this device is kept. ")

name = name.strip()
description = description.strip()
location = location.strip()

plf = platform.system()


##########Writing to file
devicefile.write("Do not modify this configuration file on your own, use the exp.py script to modify if needed.\nThis file is needed to store the name, description and location variables needed to identify each raspberry when a user calls for help.")
devicefile.write("\n")
devicefile.write ("What follows are your device variables, make life easy for yourself and use unique names and locations.\n\n")
#Variables are stored on lines 6, 10 and 14
devicefile.write("""The name of this device (Variable stored below this line): \n%s\n\n
The description of this device (Variable stored below this line):  \n%s\n\n
The location of this device (Variable stored below this line): \n%s\n\n""" % (name, description, location))

devicefile.close()

print "Do you wish to verify the settings by opening the textfile?"
answer = raw_input("Answer with Y or N: ")
answer = answer.lower()

if answer == "n":
    print "The program will terminate, you can close this window."
    time.sleep(5)
    exit()
elif answer == "y":
    if plf == "Windows":
        wincheck()
    elif plf == "Linux":
        unixcheck()
    else:
        print "The Pi-Lib-software package wasn't designed to handle this OS, the program will terminate."
        time.sleep(5)
        exit()

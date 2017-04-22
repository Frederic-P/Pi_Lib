#!/usr/bin/env python

#Run this .py file in your PowerShell(windows) or Console (Linux), don't edit the code if you don't know what you're doing; it may (and most likely will) cause issues later on.
#SINGLE Call naar libwide.ini

######Importing dependencies
import platform
import time
import os
import subprocess
import base64
import sys
absdir = os.path.dirname(sys.argv[0])
fnm = "/libwide.ini"
fpt = str(absdir)+fnm


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


######Setting Variables
configfile = open(fpt, "w+")
URL = raw_input("What is the Internet Address of this library's catalogue? \n")
server = raw_input("What is the IP address of the Pi-Lib-server?\n")
password = raw_input("Give the master-password for Pi-Lib-software, use only numbers and letters!!.\n")
password = password.strip()

#Cipher to hide the password from viewers.
#The goal is to obscure the password in stead of storing it as a plain-text string.
#Code attribution:(DATE:25/11/2016) I modified the code shared by Stackoverflow user smehmood in an anwser to Stackoverflow user RexE (See: http://stackoverflow.com/questions/2490334/simple-way-to-encode-a-string-according-to-a-password)
encoded_chars = []
for i in xrange(len(password)):
    key = "freepilibsoftwareforeveryoneonthislovelyplanetofours"
    key_c = key[i % len(key)]
    encoded_c = chr(ord(password[i]) + ord(key_c) % 256)
    encoded_chars.append(encoded_c)
encoded_string = "".join(encoded_chars)
password =  base64.urlsafe_b64encode(encoded_string)
#End of code attribution

URL = URL.strip()
y = "http://"

if URL[0:4] != "http":
    URL = y +URL
server = server.strip()


plf = platform.system()

######Writing to file
configfile.write("Do not modify this configuration file on your own, use the 'FIRST Libwide configuration.py' script to modify if needed.\nThis file is needed to store the Pi-Lib-Password, the URL of the catalogue and the IP of the Pi-Lib-server.")
configfile.write("\n")
configfile.write ("What follows are your variables:.\n\n")
#Variables are stored on lines 6, 10 and 14
configfile.write("""The Internet Address of this library's catalogue (Variable stored below this line): \n%s\n\n
The IP address of the Pi-Lib-server (Variable stored below this line):  \n%s\n\n
The master-password for Pi-Lib-software. (Variable stored below this line): \n%s\n\n""" % (URL, server, password))

configfile.close()


#######Verification
print "Do you wish to verify the settings by opening the configuration file?"
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

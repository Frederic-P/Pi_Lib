#!/usr/bin/env python

"""Pi-Lib V2.0 Shared under MIT license
Copyright (c) <2017> <FREDERIC PIETOWSKI>

 Permission is hereby granted, free of charge, to any person
 obtaining a copy of this software and associated documentation
 files (the "Software"), to deal in the Software without
 restriction, including without limitation the rights to use,
 copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the
 Software is furnished to do so, subject to the following
 conditions:

 The above copyright notice and this permission notice shall be
 included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
"""




######Loading dependencies
from Tkinter import *
from socket import *
import os
import webbrowser
import time
import platform
import base64
absdir = os.path.dirname(sys.argv[0])
#print absdir
reldirwide = absdir + "/Configuration/libwide.ini"
reldirdev = absdir + "/Configuration/device.ini"


#####Loading .ini-file content (OK)
#get libwide.ini
libwide = open(reldirwide, "r")
libcnt = libwide.readlines()
url = libcnt[5]
server = libcnt[9]
password = libcnt[13]
libwide.close()
server = server.strip()
#get device.ini
device = open(reldirdev, "r")
devcnt = device.readlines()
devname = devcnt[5]
devdesc = devcnt[9]
devloc = devcnt[13]
device.close()
devname = devname.strip()
devdesc = devdesc.strip()
devloc = devloc.strip()




#####PSM (= Pre Structured Messages)
psm1 = "There's an issue on machine %s; with location %s; and description %s" % (devname, devloc, devdesc)
psm0 = "Issue on machine %s resolved" % (devname)

#Password popup
def get_input(variable, operation, password):
    global inp
    wi = 240
    he = 100

    pox = ((w/2) - (wi/2))
    poy = ((h/2) - (he/2))

    inp = Toplevel(bd = 15, padx = 5, pady = 5, relief = "ridge")
    inp.overrideredirect(True)
    inp.resizable(width=None, height=None)
    inp.geometry("240x100+%s+%s" % (pox, poy))
    inp.title("Get password")

    frame = LabelFrame(inp, text="Provide the Pi-Lib master password")
    frame.pack()

    entry = Entry(frame, textvariable=variable)
    entry.pack()

    entry.bind("<Return>", lambda event:platformcheck(variable, operation, password))

    okbutton = Button(inp, text="OK", command=lambda:platformcheck(variable, operation, password))
    okbutton.pack()

def platformcheck(variable, operation, password):
    passphrase = variable.get()
    password = str(password)
    #Cipher to hide the password from viewers.
    #The goal is to obscure the password in stead of storing it as a plain-text string.
    #Code attribution:(DATE:25/11/2016) I modified the code shared by Stackoverflow user smehmood in an anwser to Stackoverflow user RexE (See: http://stackoverflow.com/questions/2490334/simple-way-to-encode-a-string-according-to-a-password)
    encoded_chars = []
    for i in xrange(len(passphrase)):
        key = "freepilibsoftwareforeveryoneonthislovelyplanetofours"
        key_c = key[i % len(key)]
        encoded_c = chr(ord(passphrase[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    cipher =  base64.urlsafe_b64encode(encoded_string)
    #End of code attribution

    q = cipher.strip()
    s = str(q)
    r = password.strip()
    t = str(r)

    if s == t:
        plf = platform.system()
        if plf == "Windows":
            if operation == "c":
                close()
            elif operation == "r":
                winreboot()
            elif operation == "s":
                winshutdown()
        elif plf == "Linux":
            if operation == "c":
                close()
            elif operation == "r":
                linuxreboot()
            elif operation == "s":
                linuxshutdown()
        else:
            print "This OS is not supported"
    else:
        print "Wrong password"
    inp.destroy()

def getpass(variable, operation, password):
    get_input(variable, operation, password)
    inp.wait_window()
    data = variable.get()

#End password popup

#askforhelp popup
def askforhelp(psm1, psm0, server):
    port = 13000
    addr = (server, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    data = psm1
    UDPSock.sendto(data, addr)
    fixed(psm0, server)


def fixed(psm0, server):
    global ovl
    wiovl = 400
    heovl = 225

    poxovl = ((w/2) - (wiovl/2))
    poyovl = ((h/2) - (heovl/2))

    ovl = Toplevel(bd = 15, padx = 5, pady = 5, relief = "ridge")
    ovl.overrideredirect(True)
    ovl.resizable(width=None, height=None)
    ovl.geometry("400x225+%s+%s" % (poxovl, poyovl))
    ovl.title("Set Ok")

    ovlframe = LabelFrame(ovl, text="Click 'Ok' when the issue has been resolved")
    ovlframe.config(font ="bold")
    ovlframe.pack()

    ovlokbutton = Button(ovlframe, image = okimage, command=lambda:allclear(psm0, server))
    ovlokbutton.config(height = 150, width = 267, font = "bold")
    ovlokbutton.pack()

def allclear(psm0, server):
    port = 13000
    addr = (server, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    data = psm0+"\n\n"
    UDPSock.sendto(data, addr)
    ovl.destroy()

#UDP-code derived from: http://code.activestate.com/recipes/578802-send-messages-between-computers/ (shared under MIT license.)
#End askforhelp popup

####GUI
pilib = Tk()
pilib.title("Pi-Lib V2.0 GUI")
passphrase = StringVar()

plf = platform.system()
if plf == "Linux":
    pilib.overrideredirect(False) #having the overrideredirect enabled on RASPBIAN causes the mainloop to hinder the toplevel windows that are called upon with ASKHELP and GETPASS # bug identified on 15/12/2016 ==> fixed by using windowmanager. Program code runs fine on Windows
    pilib.geometry("{0}x{1}+0+0".format(pilib.winfo_screenwidth(), pilib.winfo_screenheight()))
else:
    pilib.overrideredirect(True) #having the overrideredirect enabled on RASPBIAN causes the mainloop to hinder the toplevel windows that are called upon with ASKHELP and GETPASS # bug identified on 15/12/2016 ==> fixed by using windowmanager. Program code runs fine on Windows
    pilib.geometry("{0}x{1}+0+0".format(pilib.winfo_screenwidth(), pilib.winfo_screenheight()))

#####responsive layout
h = pilib.winfo_screenheight()
w = pilib.winfo_screenwidth()

bh = int(h*0.028125)
bw = int(w*0.0500)

#####OS-specific Functions
def winshutdown():
    os.system("shutdown.exe -f -s -t 1")

def linuxshutdown():
    os.system("poweroff")


def winreboot():
    os.system("shutdown.exe -f -r -t 1")

def linuxreboot():
    os.system("reboot")


#####BUTTON Functions
def close():
    print "The program will terminate"
    #ASK for pass.
    time.sleep(0.5)
    pilib.destroy()

def viewcat(url):
    webbrowser.open(url)


######FRAME Programming
up = Frame(pilib, pady = int(0.005*h), padx = int(0.005*w))
up.pack(side = TOP)

down = Frame(pilib, pady = int(0.005*h), padx = int(0.005*w))
down.pack(side = BOTTOM)

#####MEDIA
rebooticon = PhotoImage(file = "%s/MEDIA/reboot.gif" %(absdir))
exiticon = PhotoImage(file = "%s/MEDIA/exit.gif" %(absdir))
askhelpicon = PhotoImage(file = "%s/MEDIA/help.gif" %(absdir))
shutdownicon = PhotoImage(file = "%s/MEDIA/poweroff.gif" %(absdir))
lookupicon = PhotoImage(file = "%s/MEDIA/lookup.gif" %(absdir))
okimage = PhotoImage(file = "%s/MEDIA/ok.gif" %(absdir))
####redefine dimensions.

h = pilib.winfo_screenheight()
w = pilib.winfo_screenwidth()

bh = int(h*0.450)
bw = int(w*0.400)

#####Buttonlayout

opencat = Button(up, text="Browse our catalogue\n\n\n", image = lookupicon, command=lambda: viewcat(url), compound="bottom")
opencat.config(height = bh, width = bw, font = "bold")
opencat.pack(side = LEFT)

askhelp = Button(up, text="Ask for help\n\n\n", image = askhelpicon, command=lambda: askforhelp(psm1, psm0, server), compound="bottom")
askhelp.config(height = bh, width = bw, font = "bold")
askhelp.pack(side=RIGHT)

shutdown = Button (down, text= "Shutdown (Password required)\n\n\n", image = shutdownicon, command=lambda: getpass(passphrase, "s", password), compound="bottom")
shutdown.config(height = bh, width = int(0.666666*bw), font = "bold")
shutdown.pack(side = RIGHT)

reboot = Button (down, text = "Reboot (Password required)\n\n\n", image = rebooticon, command=lambda: getpass(passphrase, "r", password), compound="bottom")
reboot.config(height = bh, width = int(0.666666*bw), font = "bold")
reboot.pack(side= RIGHT)

exit = Button (down, text = "Close Pi-Lib (Password required)\n\n\n", image = exiticon, command=lambda: getpass(passphrase, "c", password), compound="bottom")
exit.config(height = bh, width = int(0.666666*bw), font = "bold")
exit.pack(side = LEFT)

#tkinter mainloop
pilib.protocol("WM_DELETE_WINDOW", lambda: getpass(passphrase, "c", password))      #Windowmanager
pilib.mainloop()

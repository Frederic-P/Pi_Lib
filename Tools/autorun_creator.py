#!/usr/bin/env python


import time
import getpass
import sys
import os

username = getpass.getuser()
absdir = os.path.dirname(sys.argv[0])
absdir = absdir[0:-6]


runname = "/Pi-Lib.pyw"

atspath = "/home/%s/.config/lxsession/LXDE-pi/autostart" %(username)
pywloc = absdir+runname
autostartline ="@python "+pywloc+"\n"



readcurrent = open(atspath, "r")
readcnt = readcurrent.readlines()
readcurrent.close()


memory = []

for line in readcnt:
    if len(line) > 2:
        memory.append(line)

memory.insert(0, autostartline)

print memory

overwritecurrent = open(atspath, "w")
lenmem = len(memory)
for x in range(lenmem):
    overwritecurrent.write("%s" %(memory[x]))

overwritecurrent.close()


print "Autostart entry created for user %s." %(username)
print "Program will terminate"
time.sleep(5)
exit()

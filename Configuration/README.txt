VERSION: 1.4

###########################################################################
###########################################################################
###############        RUNNING THE PROGRAM (FOR PI)         ###############
###########################################################################
1) Double click the appropriate .py file
2) Follow the instructions in the LXterminal

###########################################################################
###########################################################################
###############      RUNNING THE PROGRAM (ON WINDOWS)       ###############
###########################################################################
1) Double click the appropriate .py file
2) Follow the instructions in the terminal

###########################################################################
###########################################################################
###############                  FUNCTION                   ###############
###########################################################################

These files hold the settings for your Pi-Lib distribution.
Do not alter the content of these files unless you are 100% certain of what you're doing.

Libwide.ini stores:
- The URL of your Library
- The IP adress of your Pi-Lib server
- The Pi-Lib elevated privileges password

Device.ini stores:
- The Name of the specific device
- The physical location of the specific device
- The description of the specific device


###########################################################################
###########################################################################
###############                   CHANGELOG                 ###############
###########################################################################

FROM V1.0 to V1.1
- Splitting long strings over multiple lines:
	* Allows for simpler file input methods in Python.

###########################################################################

From V1.1 to V1.2
- Splitting a single config.ini file into Device.ini and Libwide.ini:
	* Allows for a more efficient workflow.
	* Requies less work by Library-personel.

###########################################################################

From V1.2 to V1.3: Applies to device.ini and libwide.ini configurators
- Fixing a bug where the program would not work on UNIX-systems
- Appending platformcheck
- Forking the verrification process with two new functions
	- One for Windows-OS
	- One for Linux-OS

###########################################################################

From V1.3 to V1.3.1: Applies to libwide.ini configurator
- Password no longer stored as plaintext, it's now protected by a Vigenèrecipher.

###########################################################################

From V1.3.1. to V1.4: Applies to libwide.ini configurator
- Fixes a bug where UNIX-systems read the URL-variable as a local adress in stead of a Internet adress

###########################################################################
###########################################################################
###############                KNOWN ISSUES                 ###############
###########################################################################

None (as of 14/12/2016)

###########################################################################
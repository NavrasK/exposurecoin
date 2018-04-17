# Run this program first

# Checks for uninstalled requirements and will install them with different commands based on the user's OS

import sys
import client
import os

os.system('clear')

if sys.platform.startswith('win32'): # Windows device
    # TODO: import as (pip3 install NAME)
    print("Windows System Detected")
    operatingsys = "win"

elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'): # Linux / MacOS device
    # TODO: import as (sudo pip3 install NAME)
    print("Linux / MacOS System Detected")
    operatingsys = "linmac"

else:
    # TODO: just try the linux method to see if it works, if it doesn't, throw an error and quit
    print("Unknown / Unsupported OS, will try to handle as a Linux based system")
    operatingsys = "linmac"

# NOTE: As of right now it seems that the command pip3 is the safest way for both operating systems.
#       MacOS is untested but should be the same as Linux. Cygwin and other operating systems are not 
#       tested for and will try the standard linux based commands.  

if operatingsys == "win":
    iswin = True
else:
    iswin = False

print("\nWelcome to EXPOSUREcoin! \n-Created by Navras Kamal\n")
client.Client(iswin)

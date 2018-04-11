# Run this program first

# Checks for uninstalled requirements and will install them with different commands based on the user's OS

import sys

if sys.platform.startswith('win32'): # Windows device
    # TODO: import as (pip3 install NAME)
    print("Windows")

elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'): # Linux / MacOS device
    # TODO: import as (sudo pip3 install NAME)
    print("Linux / MacOS")

else:
    # TODO: just try the linux method to see if it works
    print("Unknown / Unsupported OS")

# NOTE: As of right now it seems that the command pip3 is the safest way for both operating systems.
#       MacOS is untested but should be the same as Linux. Cygwin and other operating systems are not 
#       tested for and will try the standard linux based commands.  

# This the first program the user should

# Check if the prerequisite packages are installed, if they are not then install them

import os
import time
from client_ import main

try:
    import msgpack
except ImportError:
    print("Installing msgpack in 3 seconds [quit via interrupt to cancel]")
    time.sleep(4)
    os.system('sudo pip3 install msgpack')

try:
    import yaml
except ImportError:
    print("Installing pyyaml in 3 seconds [quit via interrupt to cancel]")
    time.sleep(4)
    os.system('sudo pip3 install pyyaml')

try:
    import bs4
except ImportError:
    print("Installing BeautifulSoup in 3 seconds [quit via interrupt to cancel]")
    time.sleep(4)
    os.system('sudo pip3 install beautifulsoup4')

try:
    import rsa
except ImportError:
    print("Installing PyCrypto in 3 seconds [quit via interrupt to cancel]")
    time.sleep(4)
    os.system('sudo pip3 install rsa')

try:
    import bluelet
except ImportError:
    print("Installing Bluelet in 3 seconds [quit via interrupt to cancel]")
    time.sleep(4)
    os.system('sudo pip3 install bluelet')

main()

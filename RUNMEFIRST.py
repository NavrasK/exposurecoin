# This the first program the user should

# Check if the prerequisite packages are installed, if they are not then install them

import os
import time
from client_ import main

try:
    import msgpack
except ImportError:
    print("Installing msgpack-python in 3 seconds [quit via interrupt to cancel]")
    time.sleep(4)
    os.system('sudo pip3 install msgpack-python')

try:
    import yaml
except ImportError:
    print("Installing yaml in 3 seconds [quit via interrupt to cancel]")
    time.sleep(4)
    os.system('sudo pip3 install yaml')

try:
    import bs4
except ImportError:
    print("Installing BeautifulSoup in 3 seconds [quit via interrupt to cancel]")
    time.sleep(4)
    os.system('sudo pip3 install beautifulsoup4')

main()

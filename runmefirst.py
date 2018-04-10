import os
import time
from client import main

try:
    import msgpack
except ImportError:
    print("Installing msgpack-python in 3 seconds [quit via interrupt to cancel]")
    time.sleep(4)
    os.system('sudo pip3 install msgpack-python')

main()

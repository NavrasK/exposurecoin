import os
from client import main

try:
    import msgpack
except ImportError:
    os.system('sudo pip3 install msgpack-python')
    print("Installing msgpack-python")

main()
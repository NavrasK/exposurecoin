# Networking 2.0 for testing purposes

# This only handles local networking and is purely for demonstration, 
# as interdevice communication did not work on the VM

import socket
import pprint
import sys
import os
import Queue
import time
import threading as threader
from handler_ import PastebinHandler as PBH
try:
    import msgpack 
except:
    raise ImportError("Install msgpack with 'sudo pip3 install msgpack'")
try:
    import bluelet
except:
    raise ImportError("Install bluelet with 'sudo pip3 install bluelet'")

class netThread(threader.Thread):
    def __init__(self, threadID, q):
        threader.Thread.__init__(self)
        self.threadID = threadID
        self.q = q
    def run(self):
        print('bleh')

class Network():
    def __init__(self, data):
        self.ip = '127.0.0.1' # Localhost
        self.bin = PBH
        self.peers = {}
        self.print_lock = threader.Lock()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(('', 0))
        with self.print_lock:
            print('Listening for peers @ UDP port %s' % self.s.getsockname()[1])

    def start_socket(self):
        print("starting")
        threader._start_new_thread(self.socket_thread(), ())
        print("ending")

    def socket_thread(self):
        while True:
            in_data, in_addr = self.s.recvfrom(65536)
            data = msgpack.unpackb(in_data)
            with self.print_lock:
                pprint.pprint((in_addr, data))
            return True

    def spinner(self):
        while True:
            for cursor in '-\\|/':
                time.sleep(0.1)
                sys.stdout.write('\r{}'.format(cursor))
                sys.stdout.flush()

if __name__ == "__main__":
    net = Network({})
    threader._start_new_thread(net.start_socket, ())
    print("DONE")

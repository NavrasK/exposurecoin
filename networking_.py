# Networking 2.0 for testing purposes

# This only handles local networking and is purely for demonstration, 
# as interdevice communication did not work on the VM

import socket
import pprint
import threading as thread
try:
    import msgpack 
except:
    raise ImportError("Install msgpack with 'sudo pip3 install msgpack-python'")

class Network():
    def __init__(self):
        self.ip = '127.0.0.1' # Localhost
        self.peers = {}
        self.print_lock = thread.Lock()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(('', 0))
        with self.print_lock:
            print('Listening for peers @ UDP port %s' % self.s.getsockname()[1])
        thread._start_new_thread(self.socket_thread, ())
    def socket_thread(self):
        while True:
            in_data, in_addr = self.s.recvfrom(65536)
            data = msgpack.unpackb(in_data)
            with self.print_lock:
                pprint.pprint((in_addr, data))

# The custom sockets system for networking purposes

# Currently a test file for working, successful methods will be addded to networking_ before final build

# Tutorials from sentdex (https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ) and Gareth Nelson
# (https://steemit.com/cryptocurrency/@garethnelsonuk/creating-a-toy-cryptocurrency-part-2a-p2p-networking)

import socket
import pprint
import threading as thread
try:
    import msgpack 
except:
    raise ImportError("Install msgpack with 'sudo pip3 install msgpack-python'")

# example_files = {'testing.txt':'This is a tessst', "linkinpark.mp3.exe":"100 percent legit"}

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind(('', 0))

# print("Listening for peers @ UDP port %s" % s.getsockname()[1])

# while True:
#     in_data, in_addr = s.recvfrom(65536)
#     print("Got a packet from %s" % str(in_addr))
#     try:
#         data = msgpack.unpackb(in_data)
#         pprint.pprint(data)
#     except:
#         print("ERROR: Could not unpack from peer")

# class FileShareNode:
#     def __init__(self, data):
#         self.file_content = data
#         self.s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#         self.s.bind(('',0))
#         print('Listening for peers @ UDP port %s' % self.s.getsockname()[1])
#         thread._start_new_thread(self._sock_thread,())
#     def handle_ping(self, in_data, addr):
#         reply_data = msgpack.packb({'msgtype':'pong', 'replyto':in_data['msgid']})
#         self.s.sendto(reply_data, addr)
#     def _sock_thread(self):
#         while True:
#             in_data, in_addr = self.s.recvfrom(65536) 
#             data = msgpack.unpackb(in_data)
#             pprint.pprint((in_addr, data))

# if __name__ == "__main__":
#     node = FileShareNode({})

'''
my_ip = '137.186.75.147'
jesse_ip = '68.151.31.79'
my_vm = 44567
jesse_host = 54132
jesse_vm = 46691
'''

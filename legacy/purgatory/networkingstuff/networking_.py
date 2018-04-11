# Handles inter-computer communication

# TODO: somethings!

# Note the information to be transmitted include at least the ending of new pastebin URLs along with an identifier to show which file is being updated, and a request function which causes all other devices on the network to pass in their stored values

# References:
# https://steelkiwi.com/blog/working-tcp-sockets/

import socket
import threading
from bitio import BitWriter

NUM_CONNECTIONS = 5
PORT = 50000  # Possible major problem: How do we know what ports each person will be using? Possibly just hardcode this on each separate machine? I suppose that wouldn't work when they test it. 

# NOTE:
# Have some function called after a file is recieved that decompresses it and saves with appropriate naming

class Network():
    def __init__(self):
        print("TEMPORARY INITIALIZATION FOR NETWORK")

# class Network1(threading.Thread):
#     def __init__(self, PORT):
#         threading.Thread.__init__(self)
#         self._PORT = PORT
#         self.sock = socket.socket()
#         self.sock.bind((socket.gethostname(), self._PORT))
#         self.sock.setblocking(0)
#         self.sock.listen(NUM_CONNECTIONS)
#         self.incoming = [self.sock]
#         self.outgoing = []
        

#     def op(self):
#         while self.incoming:
#             readable, writeable, exceptional = select.select            
#             for s in readable:
#                 if s is self.sock:
#                     connection, address = self.sock.accept()
#                     connection.setblocking(0)
#                     self.incoming.append(connection)
#                 else:  # External socket to be read from
#                     data = s.recv(8)
#                     while data:
#                         with open("recieved.txt", wb+) as save:
#                             scribe = BitWriter(save)
#                             scribe.writebits(data, 8)
#                             data = s.recv(8)
#                     # TODO call other func. that will decompress and save as another file
#                     self.incoming.remove(s)
#                     s.close()

#             for s in writeable:
        

# class Network2(threading.Thread):
#     def __init__(self, PORT):
#         threading.Thread.__init__(self)
#         # self.address = None  # Address of sender
#         # self.sender = None  # Socket to recieve data from
#         self._PORT = PORT

#     def run(self, filename):
#         with socket.socket() as s:
#             s.bind((socket.gethostname(), self._PORT))
#             s.listen(NUM_CONNECTIONS)
#             while True:
#                 sender, address = s.accept()
#                 thread.start_new_thread(on_new_sender, (sender, address))

#     def on_new_sender(self, sendersock, address):
#         with open("TIMESTAMP.txt", wb+) as save:
#             scribe = BitWriter(save)
#             # select.select returns a list 
#             data, _, _ = select.select([sendersock],[],[]) 
#             for d in data:
#                 inc = sendersock.recv(8)
#                 if inc:
#                     scribe.writebits(inc, 8)  # retrieve 8 bits at a time and write to file
#                 else:
#                     break
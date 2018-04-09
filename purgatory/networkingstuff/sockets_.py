# Now you're thinking with Sockets (testing file)

import socket
import threading
from queue import Queue

# print_lock = threading.Lock()
# q = Queue()
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_name = "google.com"

# for i in range(1,10):
#     t = threading.Thread(target = check_port)
#     t.daemon = True
#     t.start()

# for worker in range(20):
#     q.put(worker)
# q.join()

# def pscan(port):
#     try:
#         s.connect((server_name, port))
#         return True
#     except:
#         return False

# for x in range(1,26):
#     if pscan(x):
#         print("PORT " + str(x) + " IS OPEN!!!!")
#     else:
#         print("PORT " + str(x) + " IS CLOSED")


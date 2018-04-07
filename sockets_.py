# Now you're thinking with Sockets (testing file)

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_name = "pythonprogramming.net"
def pscan(port):
    try:
        s.connect((server_name, port))
        return True
    except:
        return False

for x in range(1,26):
    if pscan(x):
        print("PORT " + str(x) + " IS OPEN!!!!")
    else:
        print("PORT " + str(x) + " IS CLOSED")

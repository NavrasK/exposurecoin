# Test file

import p2p_
import asyncore

HOST = "localhost"
PORT_RANGE = range(55568, 55578)

if __name__ == "__main__":
    server = p2p_.EchoServer(HOST, PORT_RANGE)
    client = p2p_.EchoClient(HOST, PORT_RANGE)
    asyncore.loop()
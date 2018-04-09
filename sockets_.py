# Now you're thinking with Sockets (testing file)

# Tutorials from sentdex (https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ) and 
# Gareth Nelson (https://steemit.com/cryptocurrency/@garethnelsonuk/creating-a-toy-cryptocurrency-part-2a-p2p-networking)

import socket
import pprint
import msgpack

example_files = {'testing.txt':'This is a tessst', "linkinpark.mp3.exe":"100 percent legit"}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 0))

print("Listening for peers @ UDP port %s" % s.getsockname()[1])

while True:
    in_data, in_addr = s.recvfrom(65536)
    print("Got a packet from %s" % str(in_addr))
    try:
        data = msgpack.unpackb(in_data)
        pprint.pprint(data)
    except:
        print("ERROR: Could not unpack from peer")

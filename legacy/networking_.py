# Networking 2.0 for testing purposes

# This only handles local networking and is purely for demonstration, 
# as interdevice communication did not work on the VM

class Network():
    def __init__(self):
        self.ip = '127.0.0.1' # Localhost
        self.peers = {}

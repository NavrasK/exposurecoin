import rsa
import random

class Encrypt():
    def __init__(self):
        self.k = rsa
    
    def generateNonce(self):
        # Generate a random value to combine with hases
        s = ''
        for _ in range(2048):
            s += random.randint(0,1)
        return int(s)

    def pair(self):
        # Generates a public private key pair, saves private key to this object and returns public
        publickey, privatekey = rsa.newkeys(2048)
        return publickey, privatekey

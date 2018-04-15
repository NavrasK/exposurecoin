import rsa
import random
import hashlib

class Encrypt():
    def __init__(self):
        print("Encryption Active")
    
    def generateNonce(self):
        # Generate a random 1024 byte sequence it sequence to combine with hashes
        s = ''
        for _ in range(1024):
            s += random.randint(0,15)
        return int(s)

    def pair(self):
        # Generates a public private key pair, then returns them
        publickey, privatekey = rsa.newkeys(2048)
        return publickey, privatekey

    def hash(self, *args):
        # Combines all arguments together as strings in the order they are passed and returns their hash
        s = ''
        for i in args:
            s += str(i)
        return hashlib.sha256(s).hexdigest()

    def sign(self, msg, key):
        # Generally sign with the public key of the target
        msg = str(msg).encode('utf8')
        return rsa.encrypt(msg, key)

    def verify(self, msg, key):
        # Generally decode with the private key associated with the public key
        crypt = rsa.decrypt(msg, key)
        return crypt.decode('utf8')

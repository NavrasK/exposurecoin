# Handles most of the encryption

# TODO: Make the generateKeyPair properly write to file and fix the popup window, move all encryption tasks here

import hashlib as hasher
import rsa
import os
import random
# from gui_ import ClientApp

class Keys():
    def __init__(self):
        self.file_loc = "textfiles/"
        self.keys = {}
        self.refreshKeys()

    def encrypt(self, *args):
        # Performs SHA256 encryption on the input values and outputs the hashed value 
        
        s = ''
        for i in args:
            s += str(i).rstrip()
        sha256 = hasher.sha256()
        sha256.update((s).encode('utf-8'))
        return sha256.hexdigest()

    def signature(self, message, sk):
        return rsa.sign(message, sk, 'SHA256')

    def verify(self, message, signature, uid):
        self.refreshKeys()
        return rsa.verify(message, signature, self.keys[uid])

    def refreshKeys(self):
        # Checks the list of public keys and refreshes the dictionary

        self.keys = {}
        k = {}
        with open(self.file_loc + "publicKeys.txt", mode='r') as file:
            for line in file:
                uid, pk = line.rstrip().split(':')
                if uid not in k:
                    k[uid] = pk
        self.keys = k

    def generateKeyPair(self, uid):
        # Creates a public and private key pair
        pk, sk = rsa.newkeys(512)
        if not os.path.isfile(self.file_loc + "EXPkey.txt"):
            with open(self.file_loc + "EXPkey.txt", mode='a') as file:
                file.write(sk)
            with open(self.file_loc + "publicKeys.txt", mode='a') as file:
                file.write(uid + ":" + pk + "\n")
        else:
            if True:#ClientApp.overwrite_key_confirm(ClientApp):
                with open(self.file_loc + "EXPkey.txt", mode="w") as file:
                    file.truncate(0)
                    file.write(sk)
                with open(self.file_loc + "publicKeys.txt", mode='a') as file:
                    file.write(uid + ":" + pk + "\n")
                print("Deleted and Replaced")
            else:
                print("Not Deleted, process aborted")
        self.refreshKeys()

if __name__ == "__main__":
    k = Keys()
    k.generateKeyPair("TESTINGTESTINGTESTING")
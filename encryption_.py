# Handles most of the encryption

# TODO: Make the generateKeyPair properly write to file and fix the popup window, move all encryption tasks here

import hashlib as hasher
import os
import random
from gui_ import ClientApp

class Keys():
    def __init__(self):
        self.file_loc = "textfiles/"
        self.keys = {}
        self.refreshKeys()

    def encrypt(self, *args):
        s = ''
        for i in args:
            s += str(i).rstrip()
        sha256 = hasher.sha256()
        sha256.update((s).encode('utf-8'))
        return sha256.hexdigest()

    def generate_nonce(self, length):
        s = ''
        for _ in range(length):
            s += (str(random.randint(0,1)))
        return s

    def refreshKeys(self):
        self.keys = {}
        k = {}
        with open(self.file_loc + "publicKeys.txt", mode='r') as file:
            for line in file:
                uid, pk = line.rstrip().split(':')
                if uid not in k:
                    k[uid] = pk
        return k

    def generateKeyPair(self, uid):
        pk = self.generate_nonce(2048) #publickey
        sk = self.generate_nonce(2048) #secret/privatekey
        if not os.path.isfile(self.file_loc + "EXPkey.txt"):
            with open(self.file_loc + "EXPkey.txt", mode='a') as file:
                file.write(sk)
            with open(self.file_loc + "publicKeys.txt", mode='a') as file:
                file.write(uid + ":" + pk + "\n")
        else:
            if ClientApp.overwrite_key_confirm(ClientApp):
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
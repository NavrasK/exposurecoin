import os
import random
from GUI import ClientApp

class publicKeys():
    def __init__(self):
        keys = {}
        self.refreshKeys()
    def refreshKeys(self):
        self.keys = {}
        k = {}
        with open('publicKeys.txt', mode='r') as file:
            for line in file:
                uid, pk = line.rstrip().split(':')
                if uid not in k:
                    k[uid] = pk
            file.close()
        return k
    def generateKeyPair(self, uid):
        pk = '' #publickey
        sk = '' #secret/privatekey
        for _ in range(2048):
            pk.join(str(random.randint(0,1)))
            sk.join(str(random.randint(0,1)))
        print(pk)
        print(sk)
        if not os.path.isfile("EXPkey.txt"):
            with open("EXPkey.txt", mode='a') as file:
                file.write(sk)
                file.close()
            with open('publicKeys.txt', mode='a') as file:
                file.write(uid + ":" + pk + "\n")
                file.close()
        else:
            if ClientApp.overwrite_key_confirm(ClientApp):
                with open("EXPkey.txt", mode="w") as file:
                    file.truncate(0)
                    file.write(sk)
                    file.close()
                with open('publicKeys.txt', mode='a') as file:
                    file.write(uid + ":" + pk + "\n")
                    file.close()
                print("Deleted and Replaced")
            else:
                print("Not Deleted, process aborted")
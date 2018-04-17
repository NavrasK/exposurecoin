# The user object

import os
import encryption as k
import xp
import pickle

class User():
    def __init__(self, name):
        self.name = str(name) # Name is what you use to chose your account, essentially your login
        self.id = k.hash(self.name, "EXPOSURE") # Hashed version of your name to make "login" more secure
        self.public_key =  None # Initilize public / private keys
        self.private_key = None
        self.getRestoreKeys() # Restore or generate keys
        # Initilalize blockchain system
        self.blockchain = self.getChain()
        ind, prev_hash, data = self.getBlock()
        self.block = self.newBlock(ind, prev_hash, data)
        print("USER READY")
        print("Welcome " + self.name + "!")

    def getRestoreKeys(self):
        # Retreives or generates and stores a public private key pair
        if not os.path.exists('users/'+self.id):
            os.makedirs('users/'+self.id)
        with open('users/'+self.id+'/'+self.name+'.xpc', 'wb+') as file:
            file.seek(0)
            if not file.read(1):
                self.public_key, self.private_key = k.pair()
                pickle.dump(self.public_key, file)
                pickle.dump(self.private_key, file)
            else:
                file.seek(0)
                self.public_key = pickle.load(file)
                self.private_key = pickle.load(file)

    def getChain(self):
        # Assumes that the client would connect and request the chain from all user, getting the 
        # correct one. As networking isn't in the scope of this project anymore it is just going
        # to pull from a master file which is always correct for proof of concept
        chain = list()
        with open('users/MASTER/masterchain.xpc', 'r') as file:
            for _ in file:
                chain.append(pickle.load(file))
        return chain

    def getBlock(self):
        
        with open('users/MASTER/masterblock.xpc', 'r') as file:
            ind = int(file.readline())
            prev_hash = str(file.readline())
            data = []
            for _ in file:
                data.append(pickle.load(file))
            return ind, prev_hash, data

    def newBlock(self, ind, prev_hash, data):
        return xp.XP(ind, prev_hash, data)
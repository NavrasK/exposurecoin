# The user object

import os
import encryption as k
import xp
import time
import pickle

class User():
    def __init__(self, name):
        self.name = str(name) # Name is what you use to chose your account, essentially your login
        self.id = k.hash(self.name, "EXPOSURE") # Hashed version of your name to make "login" more secure
        self.public_key =  None # Initilize public / private key set
        self.private_key = None
        self.getRestoreKeys() # Restore or generate keys
        # Initilalize blockchain system
        self.blockchain = self.getChain()
        ind, prev_hash, data = self.getBlock()
        self.block = self.newBlock(ind, prev_hash, data)
        print("\nUSER READY: Welcome to EXPOSUREcoin " + self.name + "!")

    def getRestoreKeys(self):
        # Retreives or generates and stores a public private key pair
        # Note that in this system the usage of the public and private keys are switched.
        # This is because the sender encrypts their message such that anyone can decrypt it with
        # their key to verify that it was them who sent it
        if not os.path.exists('users/'+self.id):
            os.makedirs('users/'+self.id)
        with open('users/'+self.id+'/'+self.name+'.xpc', 'wb+') as file:
            file.seek(0)
            if not file.read(1):
                self.private_key, self.public_key = k.pair()
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
        with open('MASTER/masterchain.xpc', 'r') as file:
            for _ in file:
                chain.append(pickle.load(file))
        return chain

    def getBlock(self):
        # Restores the block on the master when initialized, same reasoning as in getChain
        with open('MASTER/masterblock.xpc', 'r') as file:
            ind = int(file.readline())
            prev_hash = file.readline()
        data = []
        if os.path.getsize('MASTER/mastertransactions.xpc') > 0:
            with open('MASTER/mastertransactions.xpc', 'r') as file:
                file.seek(0)
                while True:
                    try:
                        data.append(pickle.load(file))
                    except EOFError:
                        break
        return ind, prev_hash, data

    def newBlock(self, ind, prev_hash, data):
        # Creates a new block for the user
        return xp.XP(ind, prev_hash, data)

    def grindXP(self, difficulty):
        # "Grinding" XP is like mining bitcoin, it's a proof of work system
        # A certain average number of calculations are required, and the faster the user
        # completes them the more likely they are to get the reward for being the first
        # This puts a barrier up so one person will have a harder time spamming the network (in theory)
        # however in this proof of concept, this doesn't work in that, as it is purely local and each
        # user takes turn trying to guess, so spamming the network would be a "viable" scam
        seq = '0' * difficulty
        nonce = k.generateNonce()
        hashtry = k.hash(self.block, nonce)
        if hashtry[0:difficulty] == seq:
            # If the hash is approprite it saves the new values and waits for further instruction
            self.block.timestamp = time.time()
            self.block.minted = True
            self.block.nonce = nonce
            self.block.hash = hashtry
            return True
        else:
            return False

    def recieveTransaction(self, txn):
        test = k.verify(txn.verification, txn.sender.public_key)
        if test == 'EXPOSURE':
            print("\n" + self.name + " ACKNOWLEDDGES THAT " + txn.recipient.name + " RECIEVED " 
                  + str(txn.quantity) + " " + test + "coin from " + txn.sender.name)
            self.block.data.append(txn)
        else:
            raise ValueError(self.name + " RECIEVED INVALID TRANSACTION, DISCARDED")

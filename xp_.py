# The main architechture of the blockchain system.  This includes the block objects which are what is added to the chain as well as the genesis block

# TODO: If you can set it up so Genesis is a sub or superclass of XP that probably hits another note for the class material

# Note: this isn't for the tree, this is just the block object, of which there will be many.  Functions for adding this to the tree can be here, but any more should be in the blockchain_ file

import hashlib as hasher #for SHA256
import time as timer #UNIX time, since actual date/time is irrellevant compared to relative time
import random
import time
import sys

from encryption_ import Keys
from blockchain_ import WorkingTree

'''
TODO: 
SET UP MAJOR OBJECTS
Create block objects.  These will store the data for each transaction (movement of currency), a hash (based on the previous hash), a timestamp, and other info
Create consensus block chain.  This will be a list of transactions which when followed gives the current overview of ownership and movement of currency
Create transaction tree.  This will be a tree object which will take in all the incoming transactions and will be used to determine what to add to block chain
'''

userID = str(input()) #Not sure how to handle this yet but it's super important... it will track your owned currency and your actions

class Genesis():
    def __init__(self, index, origin_time, timestamp, data, hash):
        self.index = 0                      #Genesis block is block with index 0
        self.timestamp = timer.time()       #TODO: Make the time precise to milliseconds, not UNIX time

class XP(): #The blocks in the chain are called XP
    def __init__(self, index, timestamp, data, previous_hash, hash, minted, bounty, minerID):
        self.tree = WorkingTree()
        self.index = index
        self.timestamp = timer.time() #TODO: same thing as Genesis
        self.data = data
        self.transactions = {}
        self.previous_hash = previous_hash
        self.minted = False
        self.hash = self.grind_xp()
        self.k = Keys()
    def grind_xp(self):
        while(self.minted == False):
            test_hash = self.k.encrypt(self)
            if (test_hash[0]=='a' and test_hash[1]=='b' and test_hash[2]=='c' \
                and test_hash[3]=='1' and test_hash[4]=='2' and test_hash[5]=='3'):
                if self.minted == False:
                    self.minted = True
                    self.minerID = userID
                    return test_hash
    def getNonce(self, len):
        nonce = ''
        for _ in range(len):
            nonce.join(str(random.randint(0,9)))
        return str(nonce)

    def spinner(self):
        while True:
            for cursor in '-\\|/':
                time.sleep(0.1)
                sys.stdout.write('\r{}'.format(cursor))
                sys.stdout.flush()

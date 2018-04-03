# The main architechture of the blockchain system

import hashlib as hasher #for SHA256
import time as timer #UNIX time, since actual date/time is irrellevant compared to relative time
import random

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
        self.origin_time = timer.time()     #Origin time is the actual time when the chain started
        self.timestamp = 0                  #Time is the relative time from the origin time in seconds

class XP(): #The blocks in the chain are called XP
    def __init__(self, index, timestamp, data, previous_hash, hash, minted, bounty, minerID):
        self.index = index
        self.timestamp = timer.time() - AcceptedChain[0].origin_time
        self.data = data
        self.previous_hash = previous_hash
        self.minted = False
        self.hash = self.grind_xp()
    def grind_xp(self):
        while(self.minted == False):
            test_hash = self.hash_xp()
            if (test_hash[0]=='a' and test_hash[1]=='b' and test_hash[2]=='c' and test_hash[3]=='1' and test_hash[4]=='2' and test_hash[5]=='3'):
                if self.minted == False:
                    self.minted = True
                    self.minerID = userID
                    return test_hash
    def hash_xp(self):
        sha256 = hasher.sha256()
        sha256.update(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.getNonce(random.randint(40,50))))
        return sha256.hexdigest()
    def getNonce(self, len):
        nonce = ''
        for _ in range(len):
            nonce.join(str(random.randint(0,9)))
        return str(nonce)

AcceptedChain = list()

class WorkingTree():
    def __init__(self, last_transaction):
        self.last_transaction = AcceptedChain[-1]

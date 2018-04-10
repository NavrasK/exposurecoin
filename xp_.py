# The main architechture of the blockchain system.  This includes the block objects which are what is added to the chain as well as the genesis block

# TODO: If you can set it up so Genesis is a sub or superclass of XP that probably hits another note for the class material

# Note: this isn't for the tree, this is just the block object, of which there will be many.  Functions for adding this to the tree can be here, but any more should be in the blockchain_ file

import hashlib as hasher #for SHA256
import time as timer #UNIX time, since actual date/time is irrellevant compared to relative time
import random
import time
import sys
import json
import threading

from encryption_ import Keys as encryptor
from blockchain_ import WorkingTree

'''
TODO: 
SET UP MAJOR OBJECTS
Create block objects.  These will store the data for each transaction (movement of currency), a hash (based on the previous hash), a timestamp, and other info
Create consensus block chain.  This will be a list of transactions which when followed gives the current overview of ownership and movement of currency
Create transaction tree.  This will be a tree object which will take in all the incoming transactions and will be used to determine what to add to block chain
'''


    

userID = str(input()) #Not sure how to handle this yet but it's super important... it will track your owned currency and your actions

def threaded(fn):
    def wrapper(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs).start()
    return wrapper

def createGenesis():
    # The genesis block is a special block which contains the initial state of the system
    timestamp = timer.time()       #TODO: Make the time precise to milliseconds, not UNIX time
    contents = {u'blockNum': 0, u'previousHash': None, u'timestamp':timestamp, u'numTxn': 0, u'transactions':None}
    hash = encryptor.encrypt(json.dumps(contents, sort_keys=True))

    return {u'hash':hash, u'contents':contents}

class XP():
    # The blocks in the chain are called XP
    
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
        # Tries to find the SHA256 Hash which begins with the sequence 'abc123'
        # TODO Find the probability of this happening for mining time analysis

        while(self.minted == False):
            test_hash = self.k.encrypt(self)
            if (test_hash[0]=='a' and test_hash[1]=='b' and test_hash[2]=='c' \
                and test_hash[3]=='1' and test_hash[4]=='2' and test_hash[5]=='3'):
                if self.minted == False:
                    self.minted = True
                    self.minerID = userID
                    return test_hash

    def spinner(self):
        # Displays a spinning cursor while mining to show a process is running
        # TODO probably want to multi-thread this otherwise this will cause mining to take MUCH longer

        while True:
            for cursor in '-\\|/':
                time.sleep(0.1)
                sys.stdout.write('\r{}'.format(cursor))
                sys.stdout.flush()

class XPcoin():
    difficulty = 3

    def __init__(self, chain = None, transactions = None):
        self.chain = chain
        self.transactions = transactions
        self.minted = False
        self.minerID = None

        previous = chain[-1]
        previousHash = previous[u'hash']
        num = previous[u'contents'][u'blockNum'] + 1
        self.contents = {u'blockNum':num, u'previousHash':previousHash}


    def addTransactions(self, transactions):
        self.transactions.update(transactions)
        pass
        # txn = rec.pk + amount + self.sk


    # TODO: What if transactions == None?
    @threaded
    def grind_xp(self, value, userID):
        testHash = encryptor.encrypt(str(json.dumps(transactions, sort_keys=True)) + str(value))
        code = '0' * difficulty
        if testHash[0:difficulty] == code:
            self.minted = True
            # add txn with user gaining free money
            self.minerID = userID
            self.levelUP()

    def levelUP(self):
        self.contents.update({u'timestamp':timer.time(), u'numTxn':len(self.transactions), u'transactions':self.transactions})
        hash = encryptor.encrypt(self.contents)
        return {u'hash':hash, u'contents':contents}



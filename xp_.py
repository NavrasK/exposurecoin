# The main architechture of the blockchain system.  This includes the block objects which are what is added to the chain as well as the genesis block

# TODO: If you can set it up so Genesis is a sub or superclass of XP that probably hits another note for the class material

# Note: this isn't for the tree, this is just the block object, of which there will be many.  Functions for adding this to the tree can be here, but any more should be in the blockchain_ file

import hashlib as hasher #for SHA256
# import random
import time as timer
# import sys
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
    difficulty = 3

    def __init__(self, chain = None, transactions = None):
        self.chain = chain
        self.transactions = transactions
        self.minted = False
        self.minerID = None

        previous = chain[-1]
        previousHash = previous[u'hash']
        self.num = previous[u'contents'][u'blockNum'] + 1
        self.contents = {u'blockNum':num, u'previousHash':previousHash}

    def __str__(self):
        return str(self.num)


    def addTransactions(self, transactions):
        self.transactions.update(transactions)
        pass
        # txn = rec.pk + amount + self.sk

    # TODO: What if transactions == None?
    @threaded
    def grind_xp(self, value, userID):
        if self.transactions is None:
            # add free monies
            pass
        else:
            testHash = encryptor.encrypt(str(json.dumps(self.transactions, sort_keys=True)) + str(value))
            code = '0' * XP.difficulty
            if testHash[0:XP.difficulty] == code:
                self.minted = True
                # add txn with user gaining free money
                self.minerID = userID
                self.levelUP()

    def levelUP(self):
        self.contents.update({u'timestamp':timer.time(), u'numTxn':len(self.transactions), u'transactions':self.transactions})
        hash = encryptor.encrypt(self.contents)
        return {u'hash':hash, u'contents':self.contents}



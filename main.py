import hashlib as hasher
import time as timer

'''
TODO: 
SET UP MAJOR OBJECTS
Create block objects.  These will store the data for each transaction (movement of currency), a hash (based on the previous hash), a timestamp, and other info
Create consensus block chain.  This will be a list of transactions which when followed gives the current overview of ownership and movement of currency
Create transaction tree.  This will be a tree object which will take in all the incoming transactions and will be used to determine what to add to block chain
'''

class Genisis():
    def __init__(self, index, origin_time, time, data, hash):
        self.index = 0
        self.origin_time = timer.time()
        self.time = 0

class Block():
    def __init__(self, index, time, data, previous_hash, hash):
        self.index = index
        self.time = timer.time() - AcceptedChain[0].origin_time
        self.data = data
        self.previous_hash = previous_hash

AcceptedChain = list()

class WorkingTree():
    def __init__(self, last_transaction):
        self.last_transaction = AcceptedChain[-1]

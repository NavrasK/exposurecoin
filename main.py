import hashlib as hash
'''
TODO: 
SET UP MAJOR OBJECTS
Create block objects.  These will store the data for each transaction (movement of currency), a hash (based on the previous hash), a timestamp, and other info
Create consensus block chain.  This will be a list of transactions which when followed gives the current overview of ownership and movement of currency
Create transaction tree.  This will be a tree object which will take in all the incoming transactions and will be used to determine what to add to block chain
'''

class Block():
    def __init__(self, index, time, data, previous_hash):
        self.index = index
        self.time = time
        self.data = data
        self.previous_hash = previous_hash
        

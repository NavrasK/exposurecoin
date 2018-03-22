import hashlib as hash

class Block():
    def __init__(self, index, time, data, previous_hash):
        self.index = index
        self.time = time
        self.data = data
        self.previous_hash = previous_hash
        

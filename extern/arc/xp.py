import time

class XP():
    def __init__(self, ind, prev_hash, data, hash, nonce):
        self.index = ind
        self.prev_hash = prev_hash()
        self.timestamp = time.time()
        self.data = data
        self.hash = hash
        self.nonce = nonce

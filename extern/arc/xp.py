import time

class XP():
    def __init__(self, ind, prev_hash, data, hash, nonce):
        self.index = ind                # This blocks index on the blockchain
        self.prev_hash = prev_hash()    # The previous blocks hash
        self.timestamp = time.time()    # The time this block was created
        self.data = data                # Contains a list of transaction objects
        self.hash = hash                # This blocks hash, following the proof of work
        self.nonce = nonce              # The nonce that created the accepted hash for this block

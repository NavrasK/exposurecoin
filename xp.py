# all the guts of the cryptocoin

import time
import encryption as k

class XP():
    def __init__(self, ind, prev_hash, data):
        self.index = ind                # This blocks index on the blockchain
        self.prev_hash = prev_hash      # The previous blocks hash
        self.data = data                # Contains a list of transaction objects
        self.numTransactions = 0        # Block will need to be minted if this is equal to 4 transactions
        self.minted = False             # The block is only minted when it contains enough transactions
        self.timestamp = None           # The time this block was mined
        self.hash = None                # This blocks hash, following the proof of work
        self.nonce = None               # The nonce that created the accepted hash for this block
        

    def getTransactions(self):
        # Returns a list of transactions stored in the block data
        trx = {}
        for i in self.data:
            trx = self.updateTransactions(trx, i.getTransaction)
        return trx

    def updateTransactions(self, trxlist, transaction):
        # Modifies total balance of a user referenced in the transaction
        for i in transaction:
            if i in trxlist:
                trxlist[i] += transaction[i]
            else:
                trxlist[i] = transaction[i]
        return trxlist

class Transaction():
    def __init__(self, sender, recipient, quantity):
        self.sender = sender
        self.recipient = recipient
        self.quantity = int(quantity)

    def getTransaction(self):
        # Returns a dictionary with two entries, showing that the sender loses as much currency
        # as the recipient will gain.  NOTE: Transactions in EXPcoin are only in whole quantities 
        # (ie no such thing as 0.001EXP, just integers)
        return {self.sender:-(self.quantity), self.recipient:self.quantity}

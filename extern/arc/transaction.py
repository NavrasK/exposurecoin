import time

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

# NOTE: Transactions are to be signed by the private key of the sender, and can be decrypted with
#       THEIR public key only, thus they are guarenteed to be the sender of the transaction, and as
#       the only person who can send a transaction is the one losing money you cannot make false
#       transactions in someone else's name

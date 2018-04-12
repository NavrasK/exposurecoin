import time

class Transaction():
    def __init__(self, sender, recipient, quantity):
        self.sender = sender
        self.recipient = recipient
        self.quantity = quantity

# NOTE: Transactions are to be signed by the private key of the sender, and can be decrypted with
#       THEIR public key only, thus they are guarenteed to be the sender of the transaction, and as
#       the only person who can send a transaction is the one losing money you cannot make false
#       transactions in someone else's name

# The blockchain system.  This will include handling for inconsistencies between chains and the chain viewer (tree viewer)

# TODO: This is where a lot of the fraud protection will be

AcceptedChain = list()

class WorkingTree():
    def __init__(self, last_transaction):
        self.last_transaction = AcceptedChain[-1]
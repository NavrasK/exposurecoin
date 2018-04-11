# The blockchain system.  This will include handling for inconsistencies between chains and the chain viewer (tree viewer)

# TODO: This is where a lot of the fraud protection will be

class WorkingTree():
    def __init__(self):
        self.AcceptedChain = {}

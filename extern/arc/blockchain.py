import extern.arc.tree as tree
# Do we want to try anytree library instead?

class Chain():
    def __init__(self):
        self.chain = {}
        self.conflict_tree = tree

    def get_accepted(self):
        # Returns final state of transactions up until the first confict
        trx = {}
        for b in self.chain:
            trx = self.updateTransactions(trx, b.getTransactions())
        return trx

    def updateTransactions(self, trxlist, transaction):
        for i in transaction:
            if i in trxlist:
                trxlist[i] += transaction[i]
            else:
                trxlist[i] = transaction[i]
        return trxlist

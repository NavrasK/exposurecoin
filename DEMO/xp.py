# import rsa
import json
# import hashlib as hasher
import time as timer
from encryption_ import Keys as k


def verify_txn(txn):
    uid, signature, amount = txn['sender'], txn['signature'], txn['amount']

    return k.verify(amount, signature, uid=uid)


def createGenesis():
    b = Block()
    b.previous_hash = None


class Block():
    max_txn = 3  # small for demo purposes

    def __init__(self, previous_hash=None):
        self.hash = None
        self.previous_hash = previous_hash
        self.transactions = []
        self.timestamp = None
        self.full = False

    def addTransaction(self, transaction):
        # transaction of the form produced by transaction() above
        if not self.full:
            self.transactions.append(transaction)
            if len(self.transactions) == Block.max_txn:
                self.full = True
        else:
            raise ValueError('Max txn exceeded')

    def mine(self, value):
        assert self.full, "Block not full"
        diff = 3
        test_hash = k.encrpyt(str(self.previous_hash)+str(self.transactions.json.dumps(self.transactions, sort_keys=True))+str(value))
        code = '0' * diff
        if test_hash[0:diff] == code:
            self.hash = test_hash
            self.timestamp = timer.time()
            return True
        return False


class Chain():
    def __init__(self):
        self.chain = []
        self.next = Block()

    def __contains__(self, block):
        for b in self.chain:
            if b.hash == block.hash:
                return True
        return False

    def __getattr__(self, index):
        return self.chain[index]

    def addBlock(self, block, value):
        if block in self:
            return False  # maybe this should be an exception
        if block.mine(value):
            self.chain.append(block)

    def check_balances(self, accepted):
        balances = accepted
        for transaction in self.transaction_queue:
            t = transaction[1:-1]
            t.split(',')
            if t[0] not in balances:
                balances[t[0]] = -float(t[2])
            else:
                balances[t[0]] -= float(t[2])
            if t[1] not in balances:
                balances[t[1]] = float(t[2])
            else:
                balances[t[1]] += float(t[2])
        return balances

    def verify(self):
        for id, block in enumerate(self.chain):
            for txn in block.transactions:
                if not verify_txn(txn):
                    raise Exception('Invalid transaction in block {}, {}'.format(id, txn))
            if self.chain[id-1].hash != block.previousHash:
                    raise Exception('Hash inconsistency between blocks {} and {}'.format(id-1, id))

            if block.timestamp <= self.chain[id-1].timestamp:
                raise Exception('Time paradox between blocks {} and {}'.format(id-1, id))

    def check_balances(self, accepted):
        balances = accepted
        for transaction in self.transaction_queue:
           t = transaction[1:-1]
           t.split(',')
           if t[0] not in balances:
               balances[t[0]] = -float(t[2])
           else:
               balances[t[0]] -= float(t[2])
           if t[1] not in balances:
               balances[t[1]] = float(t[2])
           else:
               balances[t[1]] += float(t[2])
        return balances

# The blockchain system.  This will include handling for inconsistencies between chains and the chain viewer (tree viewer)

# TODO: This is where a lot of the fraud protection will be
from encryption_ import Keys as k
from xp_ import createGenesis
from xp_ import XP
import json

def transaction(sender_sk, sender_uid, reciever_uid, amount):
    signature = k.sign(amount, sender_sk)
    txn = {u'sender':sender_uid, u'reciever':reciever_uid, u'amount':amount, u'sig':signature}
    return txn

def verify_txn(txn):
    uid, signature, amount = txn['sender'], txn['signature'], txn['amount']

    return k.verify(amount, signature, uid)

class WorkingTree():
    def __init__(self):
        self.chain = []
        self.append(createGenesis())

        self.next = XP()

    def append(self, block):
        self.chain.append(block)

    def __getattr__(self, index):
        return self.chain[index]

    def _verifyBlockHash(self, block):
        expected = k.encrypt(json.dumps(block, sort_keys=True))
        return expected == block['hash']

    def verify(self):
        # TODO: verify chain[0]

        for id, block in enumerate(chain[1:]):
            for txn in block[u'contents'][u'transactions']:
                if not verify_txn(txn):
                    raise Exception('Invalid transaction in block {}, {}'.format(block, txn))

            if not self._verifyBlockHash(block):
                raise Exception('Invalid block hash at block {}'.format(block))

            if chain[id-1]['hash'] != block['contents']['previousHash']:
                raise Exception('Hash inconsistency between blocks {} and {}'.format(chain[id-1], block))

        return True
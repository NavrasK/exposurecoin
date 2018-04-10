import rsa
import random

class User():
    def __init__(self, id):
        self.pk, self.sk = rsa.newkeys(512)  # 512 is the size of keys, docs said 512 for sha256
        # self.id = self.generate_id()
        self.id = id
        self.transaction_queue = []

    def sign(self, message):
        return rsa.sign(message, self.sk, 'SHA256')

    def generate_id(self):
        s = ''
        for _ in range(2048):
            s += random.randint(0,1)
        return s

    def check_balances(self):
        balances = {}
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

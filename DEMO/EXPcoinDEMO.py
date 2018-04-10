# The main DEMO file, showing the way that a cryptocurrency works!

import time
import sys
import rsa
from user import User

valid_cmd = {"balances" : "Refreshes and displays the total balance for all users", \
             "chain" : "Displays the current state of the blockchain for the selected user" , \
             "queue" : "Displays the current transaction queue for the selected user", \
             "legit" : "Creates a new legitimate transaction, broadcast to all users", \
             "incomp" : "Creates an incomplete transaction, broadcast only to the sender and reciever", \
             "mint" : "Causes each user to generate a block with their current transaction list"}

a = User('a')
b = User('b')
c = User('c')
d = User('d')
s = User('s')
users = {a.id:a, b.id:b, c.id:c, d.id:d, s.id:s}

def intro():
    print("\nLOADING>>>")
    spinner(2)
    print("\rWelcome to the EXPcoin Demo Progam!")
    print("This is a program to demonstrate how a cryptocurrencies work")

def help():
    print("\nThere is 4 other virtual users on the network")
    print("For simplicity, these users are A, B, C, and D.  You are S.")
    print("\nTo view user balances enter 'balances'")
    print("To view the blockchain / conflict tree enter 'chain'")
    print("To view the transaction queue enter 'queue'")
    print("To enter a legitmiate transaction enter 'legit'")
    print("To enter an incomplete transaction enter 'incomp'")
    print("TO cause a block to be minted by each user with the current transactions enter 'mint'")

def prompt_in():
    print("\n Enter a command or enter 'help' to view all commands:")
    cmd = str(input(">>> ").rstrip()).lower()
    return cmd

def check_user(u, default = 's'):
    if u not in ['a', 'b', 'c', 'd', 's']:
        u = default
    return u

def need_help(i):
    print("INVALID INPUT")
    i += 1
    if i >= 3:
        help()
        i = 0
    return i


def format_transaction(sender_sk, sender_uid, reciever_uid, amount):
    signature = k.sign(amount, sender_sk)
    txn = {u'sender': sender_uid, u'reciever': reciever_uid, u'amount': amount, u'sig': signature}
    return txn


def new_transaction():
    i = 0
    while True:
        trx_from = str(input("FROM:").rstrip().lower())
        trx_from = str(check_user(trx_from, None))
        if trx_from is not None:
            break
        else:
            i = need_help(i)
            continue
    i = 0
    while True:
        trx_to = str(input("TO:").rstrip().lower())
        trx_to = str(check_user(trx_to, None))
        if trx_to is not None:
            break
        else:
            i = need_help(i)
            continue
    i = 0
    while True:
        trx = float(input("AMOUNT:").rstrip())
        if trx > 0.0:
            break
        else:
            i = need_help(i)
            continue

    transaction = format_transaction(users[trx_from].sk, trx_from, trx_to, trx)
    return transaction

def broadcast(transaction, targets = ['a', 'b', 'c', 'd', 's']):
    for target in targets:
        if target in users:
            users[target].transaction_queue.append(transaction)

def verify_signature(self, message, signature, uid):
    self.refreshKeys()
    return rsa.verify(message, signature, self.keys[uid])

def view_chain(u):
    print("VIEWING CHAIN")

def view_queue(u):
    print("VIEWING QUEUE")

def handle_cmd():
    i = 0
    while True:
        cmd = prompt_in()
        if cmd in valid_cmd:
            break
        else:
            i = need_help(i)
            continue
    print(valid_cmd[cmd])
    if cmd == 'balances':
        print("CURRENT BALANCE: \n" + s.check_balances())

    elif cmd == 'chain':
        print("View chain for which user? (Default: You)")
        u = str(input(">>> ").rstrip().lower())
        u = check_user(u)
        view_chain(u)

    elif cmd == 'queue':
        print("View queue for which user? (Default: You)")
        u = str(input(">>> ").rstrip().lower())
        u = check_user(u)
        view_queue(u)

    elif cmd == 'legit':
        print("Sending a legitimate transaction between two users")
        transaction = new_transaction()
        broadcast(transaction)

    elif cmd == 'incomp':
        print("Sending an incomplete transaction between two users")
        transaction = new_transaction()
        t = transaction[1:-1]
        t = t.split(',')
        broadcast(transaction, [t[0], t[1]])

    else:
        raise ValueError("COMMAND IS NOT VALID")


def spinner(len):
    t = time.time()
    while time.time()-t < len:
        for cursor in '-\\|/':
            time.sleep(0.1)
            sys.stdout.write('\r{}'.format(cursor))
            sys.stdout.flush()

intro()

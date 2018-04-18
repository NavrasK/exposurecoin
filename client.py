# The main file which links together all the parts of the project.

# The master controller for all users

import os
import pickle
import random
import shutil
import string
import sys
import time
import tkinter
import user as u
from multiprocessing.dummy import Pool as ThreadPool

import encryption as k
import xp

# NOTE: All files in extern should be totally independent of anything, or at least anything outside
#       of their group.  Their interconnection should be totally built in this file

class Client():
    def __init__(self, iswin):
        self.iswindows = iswin # Host operating system, True if running on windows, False otherwise
        # NOTE This isn't useful right now, the distinction really isn't taken into account anymore
        # Set up the user database
        self.users = {}
        print("LOGGING IN PREVIOUS USERS")
        print("This may take some time, please wait...")
        self.loginExisting()
        # The master user is essentially the admin or superuser of the network for demonstration purposes
        # It is what handles all the true consensus and gives bounty for minting coins.
        if 'MASTER' not in self.users:
            self.newUser('MASTER')
        # Start the program proper
        print("INITIALIZING>>>")
        self.spinner(length = 0.5)
        os.system('clear')
        print("CLIENT INITIALIZED")
        self.main()

    def spinner(self, length = None, step = None):
        # Displays a spinning cursor for improved user experience and to show that the process is working
        # when performing a long action such as mining a block
        if step == None:
            t = time.time()
            while time.time() - t < length:
                for cursor in '-\\|/':
                    time.sleep(0.1)
                    sys.stdout.write('\r{}'.format(cursor))
                    sys.stdout.flush()
        else:
            cursor = ['-', '\\', '|', '/']
            sys.stdout.write('\r{}'.format(cursor[step]))
            sys.stdout.flush()
            time.sleep(0.02)
        sys.stdout.write('\r')

    def loginExisting(self):
        # Goes over the existing files and logs them in on startup
        for subdir, dirs, files in os.walk('./users/'):
            for file in files:
                print("\nLogging in from " + str(subdir) + str(dirs) + str(file))
                self.newUser(file.split('.')[0])

    def newUser(self, uname = None):
        # Creates or "logs in" a user by creating and accessing files that represent that user
        if uname == None:
            uname = str(input("Enter Username: ").rstrip())
            if uname in self.users:
                print("USER ALREADY LOGGED IN")
                return
        self.users[uname] = u.User(uname)

    def generateUsers(self):
        # Generates random names for the users and checks if they aren't already used before creating a user for it
        numUsers = int(input("\nHOW MANY USERS TO GENERATE? (positive #)\n>> "))
        if numUsers > 0:
            for _ in range(numUsers):
                while True:
                    testname = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(5,8)))
                    if testname not in self.users:
                        break
                self.newUser(testname)
        else:
            print("INVALID INPUT, RETURNING TO MAIN MENU")

    def listUsers(self):
        # Displays all logged in users
        print("\nONLINE USERS:")
        for u in self.users:
            if u != 'MASTER':
                print(u)

    def newTransaction(self):
        # Sets up the variables for a new transaction and allows it to be sent to everyone (legit) or
        # to fewer than half the users (incomplete, potentially malicious)
        print("\nNEW TRANSACTION")
        self.listUsers()
        sender = str(input("\nSENDER (enter their exact name) \n>> ").rstrip())
        if sender not in self.users or sender == 'MASTER':
            print("NOT A VALID USER, RETURNING TO MAIN MENU")
            return
        recipient = str(input("RECIPIENT (enter their exact name) \n>> ").rstrip())
        if recipient not in self.users or recipient == sender or recipient == 'MASTER':
            print("NOT A VALID USER, RETURNING TO MAIN MENU")
            return
        value = float(input("AMOUNT (enter a number) \n>> "))
        if not (isinstance(value, int) or isinstance(value, float)):
            print("INVALID QUANTITY, RETURNING TO MAIN MENU")
            return
        print("\nMODE SELECT:")
        print("1: 'leg' Legitimate Transaction")
        print("2: 'inc' Incomplete Transaction")
        print("Otherwise: Cancel and return to Main Menu")
        mode = str(input("ENTER MODE (or its #) \n>> ").rstrip()).lower()
        if mode == '1' or mode == 'leg':
            self.legitTxn(self.users[sender], self.users[recipient], value)
        elif mode == '2' or mode == 'inc':
            self.fakeTxn(self.users[sender], self.users[recipient], value)
        else:
            print("\nReturning to Main Menu...")
            return
        time.sleep(5)

    def legitTxn(self, sender, recipient, value):
        # A legitimate transaction is broadcast to all or at least most users on the "network"
        ver = k.sign('EXPOSURE', sender.private_key)
        txn = xp.Transaction(sender, recipient, value, ver)
        for usr in self.users:
            self.users[usr].recieveTransaction(txn)
        with open('MASTER/mastertransactions.xpc', 'wb') as file:
            pickle.dump(txn, file)

    def fakeTxn(self, sender, recipient, value):
        # An illigitimate transaction is broadcast between the sender and recipient, only 
        # It should be automatically handled and rejected as an invalid transaction by the users over time
        ver = k.sign('EXPOSURE', sender.private_key)
        txn = xp.Transaction(sender, recipient, value, ver)
        sender.recieveTransaction(txn)
        recipient.recieveTransaction(txn)

    def grind(self):
        # Gets all users on the network to try to work out the next block that needs to be minted
        difficulty = 3
        # Requires n 0's in a row at the beginning of the hased value to be accepted
        # Each guess is random, and there is a 1/(16^n) chance per guess that the hash contains the sequence
        # The difficulty is extremely low in this case as it is all on one machine and needs to be quick
        # for demonstration rather than slow and ardous for actual use
        # Each user is iterated over once per loop in a random order.  This is because it is run locally
        # and threading is not a component of this course, thus it would be otherwise impossible
        # to demonstrate the race for users to calculate the next block, an important part of the blockchain
        # proof of work system in terms of security and accuracy
        print('This will take some time, please wait...')
        winner = None
        keys = list(self.users.keys())
        keys.remove('MASTER')
        i = 0
        step = 0
        while len(keys) > 0:
            self.spinner(step = step)
            step += 1
            if step > 3:
                step = 0
            random.shuffle(keys)
            for key in keys:
                complete = self.users[key].grindXP(difficulty)
                if complete:
                    if winner == None:
                        winner = self.users[key]
                    i += 1
                    step = 0
                    print("\r#" + str(i) +": " + key)
                    keys.remove(key)
                    break
        # Handle the winner
        for user in self.users:
            # Broadcast their blocks and mint the master block
            if user != 'MASTER':
                print("TODO")
        time.sleep(5)

    def view(self):
        # Base function for viewing information on a user or the master set
        self.listUsers()
        print("\nMODE SELECT:")
        print("1: 'master' to view Master data")
        if len(self.users) > 1:
            print("2: 'user' to view a user's data")
        print("Otherwise: Cancel and return to Main Menu")
        mode = str(input("ENTER MODE (or its #) \n>> ").rstrip()).lower()
        if mode == '1' or mode == 'master':
            self.viewMaster()
        elif (mode == '2' or mode == 'user') and len(self.users) > 1:
            self.listUsers()
            usr = str(input("\nSELECT A USER (enter their exact name) \n>> ").rstrip())
            if usr not in self.users:
                print("NOT A VALID USER, RETURNING TO MAIN MENU")
                return
            self.viewUser(usr)
        else:
            print("\nReturning to Main Menu...")
            return

    def viewMaster(self):
        # To review the contents of the master set
        print("TODO")

    def viewUser(self, user):
        # To review the contents of an individual user on the network
        print("TODO")

    def main(self):
        # This is the main control loop of the program
        while True:
            time.sleep(1)
            os.system('clear')
            self.helpText()
            print("\nMain Menu")
            cmd = str(input("ENTER COMMAND (or its #) \n>> ").rstrip()).lower()
            if cmd == '0' or cmd == 'exit':
                break
            elif cmd == '1' or cmd == 'user':
                self.newUser()
            elif cmd == '2' or cmd == 'genr':
                self.generateUsers()
            elif cmd == '3' or cmd == 'trxn':
                if len(self.users) - 1 < 2:
                    print("ERROR: NOT ENOUGH USERS ON NETWORK")
                    continue
                else:
                    self.newTransaction()
            elif cmd == '4' or cmd == 'view':
                self.view()    
            elif cmd == '5' or cmd == 'mint':
                self.grind()
            elif cmd == '275' or cmd == 'rm':
                self.resetSystem()
            else:
                print("ERROR: INVALID INPUT")
                continue
        os.system('clear')
        self.spinner(length = 0.5)
        print("Thanks for using EXPOSUREcoin!")
        time.sleep(1)
        os.system('clear')
    
    def helpText(self):
        # Shows the available commands
        print("LIST OF COMMANDS:")
        print("0: 'exit' to end the program")
        print("1: 'user' to login to or create a new user")
        print("2: 'genr' to generate a set of users randomly")
        print("3: 'trxn' to set up a transaction between users")
        print("4: 'view' to view the state of a user or Master")
        print("5: 'mint' to add the current block to the chain")
        print("275: 'rm' to delete all users & reset the system")

    def resetSystem(self):
        # Resets the entire blockchain and deletes all users
        sure = str(input("ARE YOU SURE (this cannot be undone, and will \
                            reset the blockchain) Y/N \n>> ").rstrip()).lower()
        if sure == 'y':
            # Delete everything (all users, master files and stored objects)
            shutil.rmtree('users/')
            shutil.rmtree('MASTER/')
            self.users = {}
            # Rebuild required files
            os.makedirs('users/')
            os.makedirs('MASTER/')
            with open('MASTER/masterblock.xpc', 'w+') as file:
                file.write('0\n')
                file.write('None')
            with open('MASTER/masterchain.xpc', 'w+') as file:
                pass
            with open('MASTER/mastertransactions.xpc', 'w+') as file:
                pass
            self.newUser('MASTER')
            print("SYSTEM RESET")
        else:
            print("NO ACTION TAKEN, RETURNING TO MAIN MENU...")

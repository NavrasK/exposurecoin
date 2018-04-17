# The main file which links together all the parts of the project.

# The master controller for all users

import user as u 
import xp
import encryption as k
import tkinter
import time
import sys
import os

# NOTE: All files in extern should be totally independent of anything, or at least anything outside
#       of their group.  Their interconnection should be totally built in this file

class Client():
    def __init__(self, iswin):
        self.iswindows = iswin # Host operating system, True if running on windows, False otherwise
        # Set up the user database
        self.users = {}
        # Start the program proper
        print("INITIALIZING>>>")
        self.spinner(0.5)
        os.system('clear')
        print("CLIENT INITIALIZED")
        self.main()

    def spinner(self, length):
        # Displays a spinning cursor
        t = time.time()
        while time.time() - t < length:
            for cursor in '-\\|/':
                time.sleep(0.1)
                sys.stdout.write('\r{}'.format(cursor))
                sys.stdout.flush()
        sys.stdout.write('\r')

    def newUser(self):
        # Creates or "logs in" a user
        uname = str(input("Enter Username: ").rstrip())
        self.users[uname] = u.User(uname)

    def listUsers(self):
        # Displays all logged in users
        print("\nONLINE USERS:")
        for u in self.users:
            print(u)

    def newTransaction(self):
        # Sets up the variables for a new transaction and allows it to be sent to everyone (legit) or
        # to fewer than half the users (incomplete, potentially malicious)
        print("\nNEW TRANSACTION")
        self.listUsers()
        sender = str(input("\nSENDER (enter their exact name) \n>> ").rstrip())
        if sender not in self.users:
            print("NOT A VALID USER, RETURN TO MAIN MENU")
            return
        recipient = str(input("RECIPIENT (enter their exact name) \n>> ").rstrip())
        if recipient not in self.users or recipient == sender:
            print("NOT A VALID USER, RETURN TO MAIN MENU")
            return
        value = float(input("AMOUNT (enter a number) \n>> "))
        if not (isinstance(value, int) or isinstance(value, float)):
            print("INVALID QUANTITY, RETURN TO MAIN MENU")
            return
        print("\nMODE SELECT:")
        print("1: 'leg' Legitimate Transaction")
        print("2: 'inc' Incomplete Transaction")
        print("Otherwise: Cancel and return to Main Menu")
        mode = str(input("ENTER MODE (or its #) \n>> ").rstrip()).lower()
        if mode == '1' or mode == 'leg':
            self.legitTxn(sender, recipient, value)
        elif mode == '2' or mode == 'inc':
            self.fakeTxn(sender, recipient, value)
        else:
            print("\nReturning to Main Menu...")
            return

    def legitTxn(self, sender, recipient, value):
        # 
        print("\nLEGITMIATE TRANSACTION")

    def fakeTxn(self, sender, recipient, value):
        print("\nINCOMPLETE / FALSE TRANSACTION")

    def broadcastTransaction(self):
        print("TODO")

    def view(self):
        print("\nMODE SELECT:")
        print("1: 'master' to view Master data")
        if len(self.users) > 0:
            print("2: 'user' to view a user's data")
        print("Otherwise: Cancel and return to Main Menu")
        mode = str(input("ENTER MODE (or its #) \n>> ").rstrip()).lower()
        if mode == '1' or mode == 'master':
            self.viewMaster()
        elif (mode == '2' or mode == 'user') and len(self.users) > 0:
            self.viewUser()
        else:
            print("\nReturning to Main Menu...")
            return

    def viewMaster(self):
        print("TODO")

    def viewUser(self):
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
            elif cmd == '2' or cmd == 'trxn':
                if len(self.users) < 2:
                    print("ERROR: NOT ENOUGH USERS ON NETWORK")
                    continue
                else:
                    self.newTransaction()
            elif cmd == '3' or cmd == 'view':
                self.view()    
            else:
                print("ERROR: INVALID INPUT")
                continue
        os.system('clear')
        self.spinner(0.5)
        print("Thanks for using EXPOSUREcoin!")
        time.sleep(1)
        os.system('clear')
    
    def helpText(self):
        print("LIST OF COMMANDS:")
        print("0: 'exit' to EXIT")
        print("1: 'user' to login to or create a new user")
        print("2: 'trxn' to set up a transaction between users")
        print("3: 'view' to view the state of a user or Master")

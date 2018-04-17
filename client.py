# The main file which links together all the parts of the project.

# The master controller for all users

import user as u 
import xp
import encryption as k
import tkinter
import time

# NOTE: All files in extern should be totally independent of anything, or at least anything outside
#       of their group.  Their interconnection should be totally built in this file

class Client():
    def __init__(self, iswin):
        self.iswindows = iswin # Host operating system, True if running on windows, False otherwise
        # Set up the user database
        self.users = {}
        # Start the program proper
        self.main()
        print("CLIENT INITIALIZED")

    def newUser(self):
        uname = str(input("Enter Username: ").rstrip())
        self.users[uname] = u.User(uname)

    def listUsers(self):
        print("\nONLINE USERS:")
        for u in self.users:
            print(u)

    def newTransaction(self):
        print("\nNEW TRANSACTION")
        self.listUsers()
        sender = str(input("SENDER (enter their exact name) \n>> ").rstrip())
        if sender not in self.users:
            print("NOT A VALID USER, RETURN TO MAIN MENU")
            return
        recipient = str(input("RECIPIENT (enter their exact name) \n>> ").rstrip())
        if recipient not in self.users or recipient == sender:
            print("NOT A VALID USER, RETURN TO MAIN MENU")
            return
        value = input("AMOUNT (enter a number) \n>> ").rstrip()
        if not isinstance(value, int) or not isinstance(value, float):
            print("INVALID QUANTITY, RETURN TO MAIN MENU")
            return
        print("\nMODE SELECT:")
        print("1: 'leg' Legitimate Transaction")
        print("2: 'inc' Incomplete Transaction")
        print("Otherwise: Cancel and return to main menu")
        mode = str(input("ENTER MODE (or its #) \n>> ").rstrip()).lower()
        if mode == '1' or mode == 'leg':
            self.legitTxn(sender, recipient, value)
        elif mode == '2' or mode == 'inc':
            self.fakeTxn(sender, recipient, value)
        return

    def legitTxn(self, sender, recipient, value):
        print("\nLEGITMIATE TRANSACTION")

    def fakeTxn(self, sender, recipient, value):
        print("\nINCOMPLETE / FALSE TRANSACTION")

    def view(self):
        print("\nMODE SELECT:")
        print("1: 'master' to view Master data")
        print("2: 'user' to view a user's data")
        print("Otherwise: Cancel and return to main menu")
        mode = str(input("ENTER MODE (or its #) \n>> ").rstrip()).lower()
        if mode == '1' or mode == 'master':
            self.viewMaster()
        elif mode == '2' or mode == 'user':
            self.viewUser()
        else:
            return

    def viewMaster(self):
        print("TODO")

    def viewUser(self):
        print("TODO")

    def main(self):
        # This is the main control loop of the program
        while True:
            self.helpText()
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
                time.sleep(0.1)
                continue
        print("Thanks for using EXPOSUREcoin!")
    
    def helpText(self):
        print("\nINDEX OF COMMANDS:")
        print("0: 'exit' to EXIT")
        print("1: 'user' to login to or create a new user")
        print("2: 'trxn' to set up a transaction between users")
        print("3: 'view' to view the state of a user or Master")

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
        print("CLIENT INITIALIZED")
        self.iswindows = iswin # Host operating system, True if running on windows, False otherwise
        # Set up the user database
        self.users = {}
        # Start the program proper
        self.main()

    def newUser(self):
        uname = str(input("Enter Username: ").rstrip())
        self.users[uname] = u.User(uname)

    def newTransaction(self):
        print("MODE SELECT:")
        print("1: 'leg' Legitimate Transaction")
        print("2: 'inc' Incomplete Transaction")
        print("Otherwise: Return to main menu")
        mode = str(input("ENTER MODE (or its #) \n>> ").rstrip()).lower()
        if mode == '1' or mode == 'leg':
            self.legitTxn()
        elif mode == '2' or mode == 'inc':
            self.fakeTxn()
        return

    def legitTxn(self):
        print("LEGITMIATE TRANSACTION")

    def fakeTxn(self):
        print("INCOMPLETE / FALSE TRANSACTION")

    def view(self):
        print("MODE SELECT:")
        print("1: 'master' to view Master data")
        print("2: 'user' to view a user's data")
        print("Otherwise: Return to main menu")
        mode = str(input("ENTER MODE (or its #) \n>> ").rstrip()).lower()
        if mode == '1' or mode == 'master':
            self.viewMaster()
        elif mode == '2' or mode == 'user':
            self.viewUser()
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
            if cmd == '1' or cmd == 'exit':
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
                print("INVALID INPUT")
                time.sleep(0.1)
                continue
    
    def helpText(self):
        print("INDEX OF COMMANDS:")
        print("0: 'exit' to EXIT")
        print("1: 'user' to login to or create a new user")
        print("2: 'trxn' to create a transaction between two users")
        print("3: 'view' to look into a user or the current global state")

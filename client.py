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
        # Set up the user
        self.users = {}
        # Start the program proper
        self.main()

    def newUser(self):
        uname = str(input("Enter Username: ").rstrip())
        self.users[uname] = u.User(uname, self.getChain(), self.getBlock())

    def getChain(self):
        chains = []
        for u in self.users:
            chains.append(u.blockchain)

    def getBlock(self):
        blocks = []
        for u in self.users:
            blocks.append(u.block)

    def main(self):
        # This is the main loop of the program
        while True:
            print("MAIN")
            time.sleep(0.5)
            break

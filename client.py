# The main file which links together all the parts of the project.

# The master controller for all users

import user as u 
import xp
import encryption as k
import tkinter
import time
import pickle

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
        # Assumes that the client would connect and request the chain from all user, getting the 
        # correct one. As networking isn't in the scope of this project anymore it is just going
        # to pull from a master file which is always correct for proof of concept
        chain = list()
        with open('/users/MASTER/masterchain.xpc', 'r') as file:
            for _ in file:
                chain.append(pickle.load(file))
        return chain

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

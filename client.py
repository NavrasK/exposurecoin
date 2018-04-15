# The main file which links together all the parts of the project.

# Store external functions in the extern folder, in their proper category.  To reference those files do
# from extern.GROUP.FILE import FUNCTION/CLASS

import extern.arc.transaction as txn
import extern.arc.xp as xp
import extern.arc.blockchain as chain
import extern.enc.encrypt as k
import extern.usr.network as net
import extern.usr.user as u
import extern.mis.misc as misc
#import extern.gui.interface as gui # Fix the GUI fully

import tkinter
import time

# NOTE: All files in extern should be totally independent of anything, or at least anything outside
#       of their group.  Their interconnection should be totally built in this file

class Client():
    def __init__(self, iswin):
        print("CLIENT INITIALIZED")
        self.iswindows = iswin # Host operating system, True if running on windows, False otherwise
        # Set up the user
        self.user = u.User(str(input("Enter Username: ").rstrip())) # TODO Replace with a call the the GUI
        # Set up the blockchain
        self.xpchain = self.buildChain()
        self.currBlock = self.newBlock()
        # Start the program proper
        self.main()

    def main(self):
        # This is the main loop of the program
        while True:
            print("MAIN")
            time.sleep(1)

    def queryTransactions(self):
        # Gets the current transactions from all users and returns the most likely list from among them
        print("TODO")

    def buildChain(self):
        # Creates a chain and populates it with blocks from all users on the network
        xpc = chain.Chain()
        xpc.updateChain()
        return xpc

    def newBlock(self):
        # Creates a block and queries all users for the transactions to put into it
        data = self.queryTransactions()
        ind = self.xpchain.chain[-1].ind +1
        prev_hash = self.xpchain.chain[-1].hash
        nonce = k.Encrypt.generateNonce
        block = xp.XP(ind, prev_hash, data, nonce)
        return block

    def newTransaction(self):
        # The active user sends some amount of currency to another user
        send = self.user.id_key
        to = str(input("TO: ").rstrip())
        while True:
            amt = input("AMOUT YOU SEND TO "+to+" (enter 0 to cancel, positive integers only): ")
            if amt == 0:
                return False
            if isinstance(amt, int):
                if amt > 0:
                    self.currBlock.data.append(txn.Transaction(send, to, amt))
                    self.broadcastTransaction()
                    return True
            print("INVALID")

    def broadcastTransaction(self):
        # Tell all users about the transaction you just made by sending it to everyone
        print("TODO")

    def checkIncoming(self):
        # Check your "inbox" to see if there is any outgoing transactions 
        print("TODO")

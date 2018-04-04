# The client system, combining the user objects and GUI setup

from tkinter import * 

from user import User
from GUI import ClientApp

class publicKeys():
    def __init__(self):
        keys = self.readKeys()
    def readKeys(self):
        k = {}
        i = 0
        with open('publicKeyImporter.txt', mode='r') as file:
            for line in file:
                uid, pk = line.rstrip().split(':')
                if uid not in k:
                    k[uid] = pk
            file.close()
        return k
    def refreshKeys(self):
        self.keys = {}
        self.keys = self.readKeys()
    def generateKeyPair(self, uid):
        #TODO add key to public keys and generate secret key file
        self.refreshKeys()

def main():
    root = Tk()
    root.title("TEST WINDOW")
    root.config(height = 400, width = 500)

    app = ClientApp(root)

    root.mainloop()

def initialize():
    publicKeys.__init__()
    User.__init__()
    ClientApp.__init__()
    main() 

if __name__ == "__main__":
    initialize()

# The client system, combining the user objects and GUI setup

import tkinter as tk

from user import User
from GUI import ClientApp
from keys import publicKeys

#Global Vars:
root = tk.Tk()

def main():
    
    root.title("TEST WINDOW")
    root.config(height = 400, width = 500)

    app = ClientApp(root)

    root.mainloop()

    publicKeys.generateKeyPair(publicKeys, "ABC123")
    publicKeys.refreshKeys(publicKeys)

def initialize():
    pkeys = publicKeys()
    u = User()
    app = ClientApp(master=root)
    main() 

if __name__ == "__main__":
    initialize()

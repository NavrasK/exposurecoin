# The client system, combining the user objects and GUI setup

import tkinter as tk

from user_ import User
from GUI import ClientApp as cApp
from keys import publicKeys

#Global Vars:
root = tk.Tk()

def main():
    root.title("TEST WINDOW")
    root.config(height = 400, width = 500)

    app = cApp(root)

    root.mainloop()

    publicKeys.generateKeyPair(publicKeys, "ABC123")
    publicKeys.refreshKeys(publicKeys)

def initialize():
    pkeys = publicKeys()
    user = User()
    app = cApp(master=root)
    main() 

if __name__ == "__main__":
    initialize()

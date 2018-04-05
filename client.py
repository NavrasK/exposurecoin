# The client system, combining the user objects and GUI setup

import tkinter as tk

from user_ import User
from GUI import ClientApp as gui
from keys import publicKeys
from server import Server

def main():
    root = tk.Tk()

    # Initialize
    pkeys = publicKeys()
    user = User()
    app = gui(master=root)
    s = Server()

    root.title("TEST WINDOW")
    root.config(height = 400, width = 500)

    app = gui(root)

    root.mainloop()

    publicKeys.generateKeyPair(publicKeys, "ABC123")
    publicKeys.refreshKeys(publicKeys)

if __name__ == "__main__":
    main()

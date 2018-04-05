# The client system, combining the user objects and GUI setup

import tkinter as tk

from user_ import User
from gui_ import ClientApp as gui
from encryption_ import Keys
from server_ import Server

def main():
    root = tk.Tk()

    # Initialize
    keys = Keys()
    user = User()
    app = gui(master=root)
    s = Server("https://www.pastebin.com/")

    root.title("TEST WINDOW")
    root.config(height = 400, width = 500)

    app = gui(root)

    root.mainloop()

if __name__ == "__main__":
    main()

# The client system, combining the user objects and GUI setup

# This is the main program the user will run to use the network

from tkinter import *

# from user_ import User
from gui_ import ClientApp
from encryption_ import Keys
from networking_ import Network

def main():
    root = Tk()

    # Initialize
    keys = Keys()
    # user = User()
    # app = gui()
    net = Network()

    root.title("EXPCoin Client")
    # root.config(height = 400, width = 500)

    app = ClientApp(master=root)

    app.run()

if __name__ == "__main__":
    main()

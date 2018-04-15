# The main file which links together all the parts of the project.

# Store external functions in the extern folder, in their proper category.  To reference those files do
# from extern.GROUP.FILE import FUNCTION/CLASS

import extern.arc.transaction as txn
import extern.arc.xp as xp
import extern.arc.blockchain as chain
import extern.enc.encrypt as k
#import extern.gui.interface as gui # Not sure why this is happening, but fix GUI first then fix this later
import extern.net.network as net
import extern.usr.user as u
import extern.mis.misc as misc

import tkinter
import time

# NOTE: All files in extern should be totally independent of anything, or at least anything outside
#       of their group.  Their interconnection should be totally built in this file

class Client():
    def __init__(self, iswin):
        print("CLIENT INITIALIZED")
        self.iswindows = iswin # Host operating system, True if running on windows, False otherwise
        self.user = u
        self.main()

    def main(self):
        # This is the main loop of the program
        while True:
            print("MAIN")
            time.sleep(1)

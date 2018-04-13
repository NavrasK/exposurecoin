# Store external functions in the extern folder, in their proper category.  To reference those files do
# from extern.GROUP.FILE import FUNCTION/CLASS

import extern.arc.transaction
import extern.arc.xp
import extern.enc.encrypt
import extern.gui.interface
import extern.net.network
import extern.usr.user
import extern.mis.misc

# NOTE: All files in extern should be totally independent of anything, or at least anything outside
#       of their group.  Their interconnection should be totally built in this file

class Client():
    def __init__(self, iswin):
        print("CLIENT INITIALIZED")
        self.iswindows = iswin # Host operating system, True if running on windows, False otherwise

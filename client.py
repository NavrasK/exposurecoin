# Store external functions in the extern folder, in their proper category.  To reference those files do
# from extern.GROUP.FILE import FUNCTION/CLASS

class Client():
    def __init__(self, iswin):
        print("CLIENT INITIALIZED")
        self.iswin = iswin # Host operating system, True if running on windows, False otherwise

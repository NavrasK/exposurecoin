from extern.net.test import testingtesting
from extern.net.objectify import Objectify

class Client():
    def __init__(self):
        print("CLIENT INITIALIZED")
        self.obj = Objectify()
        self._test_function()

    def _test_function(self):
        print("TEST")
        testingtesting()
        self.obj.printit()

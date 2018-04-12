import pathlib
import os

class User():
    def __init__(self, id_key, p_key, pword):
        self.id_key = id_key # User ID is essentially your public key and username
        self.id_dir = '/files/'+self.id_key
        self.p_key = p_key # Key is your private key (DO NOT LOSE IT!)
        self.pword = pword

    def savekey(self):
        # NOTE: Untested as of right now, but it basically saves your private key to a file
        #       if you haven't already so that you don't lose it
        pathlib.Path(self.id_dir).mkdir(exist_ok=True)
        with open(self.id_dir + "/privatekey.txt") as file:
            file.seek(0)
            if not file.read(1):
                file.seek(0)
                file.write(str(self.p_key))

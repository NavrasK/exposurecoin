import pathlib
import os

class User():
    def __init__(self, id_key, p_key, pword):
        self.id_key = id_key # User ID is essentially your public key 
        self.dir = '/files/'+self.id_key
        self.p_key = p_key # Key is your private key (DO NOT LOSE IT!)
        self.pword = pword

    def savekeys(self):
        pathlib.Path(self.dir).mkdir(exist_ok=True)
        with open(self.dir + "/keys.txt") as file:
            file.seek(0)
            if not file.read(1):
                file.write(self.id_key+'\n'+self.p_key)
            else:
                file.seek(0)
                if self.id_key != file.readline():
                    print("OVERWRITE PUBLIC KEY??")
                if self.id_key != file.readline():
                    print("OVERWRITE PRIVATE KEY??")

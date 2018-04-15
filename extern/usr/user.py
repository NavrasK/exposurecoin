import pathlib
import os
import hashlib
import rsa

class User():
    def __init__(self, name):
        self.name = name # Name is your username and password in a way
        self.id_key =  None # IDKey is your public key
        self.dir = '/files/users/'+self.name # The path to this user's local folder
        self.p_key = None # Key is your private key (DO NOT LOSE IT!)
        self.usrkeys = {}
        self.login()
        print("User Created")

    def login(self):
        pathlib.Path(self.dir).mkdir(exist_ok=True)
        with open(self.dir+"/private.txt") as file:
            file.seek(0)
            if not file.read(1):
                file.truncate(0)
                self.newUser()
                file.write(str(self.p_key))
            else:
                file.seek(0)
                self.p_key = file.readline()
        self.getPublicId()

    def newUser(self):
        self.id_key, self.p_key = rsa.newkeys(2048)
        with open("../../../files/users/publickeys.txt", 'a') as file:
            file.write(hashlib.sha256(self.p_key+"EXPOSURE")+":"+self.id_key)
    
    def getPublicId(self):
        with open("../../../files/users/publickeys.txt", 'r') as file:
            for line in file:
                hashedkey, public = line.split(':')
                self.usrkeys[hashedkey] = public
        self.id_key = self.usrkeys[hashlib.sha256(self.p_key+"EXPOSURE")]

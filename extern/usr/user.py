import os
import hashlib
import rsa

class User():
    def __init__(self, name):
        self.name = str(name) # Name is your username and password in a way
        self.id_key =  None # IDKey is your public key
        self.p_key = None # Key is your private key (DO NOT LOSE IT!)
        self.usrkeys = {}
        print("This may take a while... please wait")
        self.login()

    def login(self):
        # Fetches the user data from their file, if they don't have one it makes one
        with open(os.path.join('extern/usr/users/', self.name+'.txt'), 'w+') as file:
            file.seek(0)
            if not file.read(1):
                file.truncate(0)
                self.newUser()
                file.write(self.p_key + '\n')
            else:
                file.seek(0)
                self.p_key = file.readline()
        self.getPublicId()
        print("User Created")

    def newUser(self):
        # Generates a new key pair for the user and stores the public key in the "server"
        # paired with an encrypted version of their private key so they can grab it later
        self.id_key, self.p_key = rsa.newkeys(2048)
        hashed = hashlib.sha256((str(self.p_key)+"EXPOSURE").encode('utf8')).hexdigest()
        writeto = hashed + ":" + self.id_key
        with open(os.path.join('extern/usr/public/', 'publickeys.txt'), 'a+') as file:
            file.write(writeto + '\n')
    
    def getPublicId(self):
        # Searches the "key server" to find the active user's public key
        with open(os.path.join('extern/usr/public/', 'publickeys.txt'), 'r+') as file:
            for line in file:
                hashedkey, public = line.split(':')
                self.usrkeys[hashedkey] = public
        self.id_key = self.usrkeys[hashlib.sha256((str(self.p_key)+"EXPOSURE").encode('utf8')).hexdigest()]

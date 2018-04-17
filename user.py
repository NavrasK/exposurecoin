# The user object

import os
import encryption as k
import pickle

class User():
    def __init__(self, name, curr_chain, curr_block):
        self.name = str(name) # Name is what you use to chose your account, essentially your login
        self.id = k.hash(self.name, "EXPOSURE") # Hashed version of your name to make "login" more secure
        self.public_key =  None # Initilize public / private keys
        self.private_key = None
        self.getRestoreKeys() # Restore or generate keys
        self.blockchain = curr_chain
        self.block = curr_block
        print("USER READY")
        print("Welcome " + self.name + "!")

    def getRestoreKeys(self):
        # Retreives or generates and stores a public private key pair
        if not os.path.exists('users/'+self.id):
            os.makedirs('users/'+self.id)
        with open('users/'+self.id+'/'+self.name+'.xpc', 'wb+') as file:
            file.seek(0)
            if not file.read(1):
                self.public_key, self.private_key = k.pair()
                pickle.dump(self.public_key, file)
                pickle.dump(self.private_key, file)
            else:
                file.seek(0)
                self.public_key = pickle.load(file)
                self.private_key = pickle.load(file)

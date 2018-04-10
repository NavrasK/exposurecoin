# Functions related to the creation and handling of users

# TODO: fix account creation, test, then remove legacy code

import hashlib as hasher
import random
from encryption_ import Keys

class User():
    def __init__(self):
        self.file_loc = "textfiles/"
        self.userID = None
        self.localBalance = None
        self.logged_in = False
        self.pk = None
        self.sk = None
        self.uname = None
        self.k = Keys()

    def login(self, uname, pword):
        # Checks the hash of the input username and password against the encrypted list to see if the user exists
        # If they do, sign them in

        credentials = self.k.encrypt(uname, pword)
        self.logged_in = False
        i = 0
        with open(self.file_loc + "usrdata.txt", mode='r') as file:
            for line in file:
                line = line.rstrip('\n')
                i += 1
                if self.logged_in:
                    return line #User ID
                elif i % 2:
                    if credentials == line:
                        self.logged_in = True
                        print("LOGGED IN!")
        if not self.logged_in:
            raise ValueError("CREDENTIALS NOT FOUND")

    def create(self, uname, pword, pword_confirm):
        # Creates a new user with the input parameters, if the user exists, log them in
        
            if not (pword == pword_confirm):
                raise ValueError("PASSWORDS DO NOT MATCH")
            else:
                self.logged_in = False
                credentials = self.k.encrypt(uname, pword)
                i = 0
                with open(self.file_loc + "usrdata.txt", mode='r') as file:
                    for line in file:
                        line = line.rstrip('\n')
                        i += 1
                        if self.logged_in:
                            self.userID = line
                            return line
                        elif i % 2:
                            if credentials == line:
                                print("ACCOUNT ALREADY EXISTS!")
                                print("LOGGING IN")
                                self.logged_in = True
                                return None  # Testing this for making GUI, if I forget to change back and it causes problems, lemme know
                if not self.logged_in:
                    print("CREATING ACCOUNT")
                    idkey = self.k.generate_nonce(2048)
                    uid = self.k.encrypt(uname, pword, idkey)
                    with open(self.file_loc + "usrdata.txt", mode='a') as file:
                        file.write(credentials+'\n')
                        file.write(uid+'\n')
                    self.logged_in = True
                    self.userID = uid
                    return uid

# Legacy code (for reference)
def terminal_authenticate():
    userid = None
    logged_in = False
    file_loc = "textfiles/"

    while not logged_in:
        have_account = str(input("Do you already have an account? (Y/N)\n"))

        if have_account == 'N' or have_account == 'n':
            uname = str(input("Enter a username:")).rstrip()
            while True:
                pword = str(input("Enter a password:")).rstrip()
                pword_confirm = str(input("Confirm Password:")).rstrip()
                if not (pword == pword_confirm):
                    print("PASSWORDS DO NOT MATCH!")
                    continue
                else:
                    break
            sha256 = hasher.sha256()
            sha256.update((uname+pword).encode('utf-8'))
            credentials = sha256.hexdigest()
            i = 0
            with open(file_loc + "usrdata.txt", mode='r') as file:
                for line in file:
                    line = line.rstrip('\n')
                    i += 1
                    if logged_in:
                        userid = line
                        break
                    elif i % 2:
                        if credentials == line:
                            print("ACCOUNT ALREADY EXISTS!")
                            print("LOGGING IN")
                            logged_in = True
            if not logged_in:
                print("CREATING ACCOUNT")
                idkey = ''
                for _ in range(random.randint(40,100)):
                    idkey.join(str(random.randint(0,9)))
                sha256.update((uname+pword+idkey).encode('utf-8'))
                uid = sha256.hexdigest()
                with open(file_loc + "usrdata.txt", mode='a') as file:
                    file.write(credentials+'\n')
                    file.write(uid+'\n')
                logged_in = True
                userid = uid
            break

        if have_account == 'Y' or have_account == 'y' and not logged_in:
            while not logged_in:
                uname = str(input("USERNAME:")).rstrip()
                pword = str(input("PASSWORD:")).rstrip()
                sha256 = hasher.sha256()
                sha256.update((uname+pword).encode('utf-8'))
                credentials = sha256.hexdigest()
                i = 0
                with open(file_loc + "usrdata.txt", mode='r') as file:
                    for line in file:
                        line = line.rstrip('\n')
                        i += 1
                        if logged_in:
                            userid = line
                            break
                        elif i % 2:
                            if credentials == line:
                                logged_in = True
                                print("LOGGED IN!")
                if not logged_in:
                    print("USER NOT FOUND!")
                    try_again = str(input("Enter Y to try again\n"))
                    if not(try_again == 'y' or try_again == 'Y'):
                        break

        else:
            print("INVALID INPUT")
    return userid

def main():
    print("WELCOME USER " + terminal_authenticate()[:9] + "(...)")

if __name__ == "__main__":
    main()

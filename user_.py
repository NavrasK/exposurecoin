# Functions related to the creation and handling of users

# TODO: fix account creation, test, then remove legacy code

import hashlib as hasher
import random
from encryption_ import Keys

k = Keys()

class User():
    def __init__(self):
        userID = None
        localBalance = None
        logged_in = False
        pk = None
        sk = None
        uname = None

    def login(self, uname, pword):
        credentials = k.encrypt(uname, pword)
        self.logged_in = False
        i = 0
        with open('usrdata.txt', mode='r') as file:
            for line in file:
                line = line.rstrip('\n')
                i += 1
                if self.logged_in:
                    return line #User ID
                elif i % 2:
                    if credentials == line:
                        self.logged_in = True
                        print("LOGGED IN!")
            file.close()
        if not self.logged_in:
            raise ValueError("CREDENTIALS NOT FOUND")

    def create(self, uname, pword, pword_confirm):
            if not (pword == pword_confirm):
                raise ValueError("PASSWORDS DO NOT MATCH")
            else:
                self.logged_in = False
                credentials = k.encrypt(uname, pword)
                i = 0
                with open('usrdata.txt', mode='r') as file:
                    for line in file:
                        line = line.rstrip('\n')
                        i += 1
                        if self.logged_in:
                            return line
                        elif i % 2:
                            if credentials == line:
                                print("ACCOUNT ALREADY EXISTS!")
                                print("LOGGING IN")
                                self.logged_in = True
                    file.close()
                if not self.logged_in:
                    print("CREATING ACCOUNT")
                    idkey = k.generate_nonce(2048)
                    uid = k.encrypt(uname, pword, idkey)
                    with open('usrdata.txt', mode='a') as file:
                        file.write(credentials+'\n')
                        file.write(uid+'\n')
                        file.close()
                    self.logged_in = True
                    return uid

# Legacy code (for reference)
def terminal_authenticate():
    userid = None
    logged_in = False

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
            with open('usrdata.txt', mode='r') as file:
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
                file.close()
            if not logged_in:
                print("CREATING ACCOUNT")
                idkey = ''
                for _ in range(random.randint(40,100)):
                    idkey.join(str(random.randint(0,9)))
                sha256.update((uname+pword+idkey).encode('utf-8'))
                uid = sha256.hexdigest()
                with open('usrdata.txt', mode='a') as file:
                    file.write(credentials+'\n')
                    file.write(uid+'\n')
                    file.close()
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
                with open('usrdata.txt', mode='r') as file:
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
                    file.close()
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

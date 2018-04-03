# The GUI for the client interface

import hashlib as hasher
import random

userid = None
logged_in = False

while True:
    have_account = str(input("Do you already have an account? (Y/N)\n"))
    if have_account == 'N':
        uname = str(input("Enter a username:"))
        while True:
            pword = str(input("Enter a password:"))
            pword_confirm = str(input("Confirm Password:"))
            if not (pword == pword_confirm):
                print("PASSWORDS DO NOT MATCH!")
                continue
            else:
                break
        sha256 = hasher.sha256()
        sha256.update(uname+pword)
        credentials = sha256.hexdigest()
        i = 0
        with open('usrdata.txt', mode='r') as file:
            for line in file:
                if logged_in:
                    userid = line
                    break
                elif not (i%2):
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
            sha256.update(uname+pword+idkey)
            uid = sha256.hexdigest()
            with open('usrdata.txt', mode='a'):
                file.write(credentials)
                file.write(uid)
                file.close()
            logged_in = True
            userid = uid
        break
    if have_account == 'Y':
        while not logged_in:
            uname = str(input("USERNAME:"))
            pword = str(input("PASSWORD:"))
            sha256 = hasher.sha256()
            sha256.update(uname+pword)
            credentials = sha256.hexdigest()
            i = 0
            with open('usrdata.txt', mode='r') as file:
                for line in file:
                    if logged_in:
                        userid = line
                        break
                    elif not (i%2):
                        if credentials == line:
                            logged_in = True
                file.close()
            if not logged_in:
                print("USER NOT FOUND!")
    else:
        print("INVALID INPUT")

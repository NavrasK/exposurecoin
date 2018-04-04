# The GUI for the client interface

import hashlib as hasher
import os
import random
from tkinter import * 

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
                    if os.stat('usrdata.txt').st_size:
                        file.write('\n')
                    file.write(credentials+'\n')
                    file.write(uid)
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
    root = Tk()
    root.geometry("500x400")
    
    frame = Frame(root)
    frame.grid()
    root.title("TESTING")

    

    root.mainloop()
    # print("WELCOME USER " + terminal_authenticate()[:9] + "(...)")

if __name__ == "__main__":
    main()

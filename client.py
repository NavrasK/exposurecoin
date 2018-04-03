# The GUI for the client interface

userid = None
logged_in = False

while True:
    makeaccount = str(input("Do you already have an account? (Y/N)")
    if makeaccount == 'Y':
        while not logged_in:
            uname = str(input("USERNAME:"))
            pword = str(input("PASSWORD:"))
            print("checking...")
            i = 0
            with open('usrdata.txt', mode='r') as file:
                for line in file:
                    if logged_in:
                        userid = line
                    elif not (i%2):
                        u, p = line.split(',')
                        if uname == u:
                            if pword == p:
                                logged_in = True
                            else:
                                print("CREDENTIALS DO NOT MATCH!")
                        else:
                            print("USER NOT FOUND!")
                            print("Would you like ")

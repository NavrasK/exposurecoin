# The GUI version of the client, will replace client.py eventually

import hashlib as hasher
import os
import random
from tkinter import *

class ClientApp(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_elements()
        self.display_login_main()
        self.logged_in = False

    def create_elements(self):
        self.main_text = Label(self, text="Welcome to the EXPcoin Client")
        self.terminal_text = Label(self, text="")
        self.uname_prompt = Label(self, text="ENTER USERNAME")
        self.pword_prompt = Label(self, text="ENTER PASSWORD")
        self.pword_confirm_prompt = Label(self, text="CONFIRM PSSWRD")

        self.uname_entry = Entry(self)
        self.pword_entry = Entry(self)
        self.pword_confirm = Entry(self)

        self.login_button = Button(self, text="LOGIN", command = self.login())
        # self.create_acct_button = Button(self, text="CREATE ACCOUNT", command = self.create_account())
        self.create_button = Button(self, text="CREATE ACCOUNT", command = self.create_user())

        self.userid = Text(self, width=30, height=5, wrap=CHAR)
        self.local_balance = Text(self, width = 30, height=5, wrap=CHAR)

    def display_login_main(self):
        self.main_text.grid(row=0, column=0, sticky=W)

        self.uname_prompt.grid(row=1, column=0, sticky=W)
        self.uname_entry.grid(row=1, column=1, columnspan=4, sticky=W)

        self.pword_prompt.grid(row=2, column=0, sticky=W)
        self.pword_entry.grid(row=2, column=2, columnspan=4, sticky=W)

        self.terminal_text.grid(row=3, columnspan=3)
        
        #self.create_acct_button.grid(row=4, column=1)
        self.login_button.grid(row=4, column=2)
    
    def display_create_account(self):
        self.main_text.grid(row=0, column=0, sticky=W)

        self.uname_prompt.grid(row=1, column=0, sticky=W)
        self.uname_entry.grid(row=1, column=1, columnspan=4, sticky=W)

        self.pword_prompt.grid(row=2, column=0, sticky=W)
        self.pword_entry.grid(row=2, column=2, columnspan=4, sticky=W)

        self.pword_confirm_prompt.grid(row=3, column=0, sticky=W)
        self.pword_confirm.grid(row=3, column=1, columnspan=4, sticky=W)

        self.terminal_text.grid(row=4, columnspan=3)
        
        #self.create_acct_button.grid(row=5, column=1)
        self.login_button.grid(row=5, column=2)

    def login(self):
        uname = self.uname_entry.get().rstrip()
        pword = self.pword_entry.get().rstrip()
        sha256 = hasher.sha256()
        sha256.update((uname+pword).encode('utf-8'))
        credentials = sha256.hexdigest()
        logged_in = False
        i = 0
        with open('usrdata.txt', mode='r') as file:
            for line in file:
                line = line.rstrip('\n')
                i += 1
                if logged_in:
                    self.userid["text"] = line
                    self.terminal_text["text"] = "LOGGED IN AS " + line
                    self.main_text["text"] = "Welcome to the EXPcoin Client User " + line[:9] + "(...)"
                    break
                elif i % 2:
                    if credentials == line:
                        logged_in = True
                        print("LOGGED IN!")
            file.close()
        if not logged_in:
            self.terminal_text["text"] = "INVALID CREDENTIALS"

    def create_account(self):
        self.display_create_account()

    def create_user(self):
        print("create account")

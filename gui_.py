# The GUI for the client

# TODO: Nuke it and start over from the top

import hashlib as hasher
import os
import random
import tkinter as tk
from tkinter import messagebox

class ClientApp(tk.Frame):
    def __init__(self, master = None):
        self.file_loc = "textfiles/"
        super().__init__(master)
        self.config(width = 500, height = 500)
        self.login_screen()
        self.pack()
        self.logged_in = False

    def login_screen(self):
        print("debug")
        self.config(padx=5, pady=5)
        self.title="EXPCoin Client"

        self.prompt = tk.LabelFrame(self, text="Login", padx=5, pady=5, width=200, height=200)
        self.prompt.pack(side="top")
        self.prompt.bind('<Return>', print("enter"))

        self.user = (tk.Label(self.prompt, text="Username: "), tk.Entry(self.prompt))
        self.pword = (tk.Label(self.prompt, text="Password: "), tk.Entry(self.prompt, show='*'))
        self.create_acc = tk.Button(self.prompt, text="Create a new account", command=self.new_acc_screen)
        self.login_button = tk.Button(self.prompt, text="Login", command=self.login)

        self.user[0].grid(row=0, column=0)
        self.user[1].grid(row=0, column=1)
        self.pword[0].grid(row=1, column=0)
        self.pword[1].grid(row=1, column=1)
        self.create_acc.grid(row=3, column=1, pady=2)
        self.login_button.grid(row=2, column=1, pady=2)

    def new_acc_screen(self):
        def validate():
            password = (self.pword[1].get().rstrip(), self.conf_pword[1].get().rstrip())
            if password[0] != password[1]:
                tk.messagebox.showinfo("Error", "Passwords do not match, try again.")
                self.pword[1].delete(0,'end')
                self.conf_pword[1].delete(0,'end')
            else:
                try:
                    self.create_account()
                except NameError:
                    self.pword[1].delete(0,'end')
                    self.conf_pword[1].delete(0,'end')

        self.prompt.config(text="Create Account")
        self.login_button.destroy()
        self.create_acc.config(command=validate, text="Create Account")
        self.conf_pword = (tk.Label(self.prompt, text="Confirm Password: "), tk.Entry(self.prompt, show='*'))
        self.conf_pword[0].grid(row=2, column=0)
        self.conf_pword[1].grid(row=2, column=1)
        self.create_acc.grid(row=3, column=1)



    def create_account(self):
        
        uname = self.user[1].get().rstrip()
        pword = self.pword[1].get().rstrip()
        sha256 = hasher.sha256()
        sha256.update((uname + pword).encode('utf-8'))
        credentials = sha256.hexdigest()
        print(credentials)
        with open(self.file_loc + "usrdata.txt", mode='r') as file:
            for line in file:
                if line == credentials:
                    raise NameError
        with open(self.file_loc + "usrdata.txt", mode='a') as file:
            file.write(credentials + '\n')
            self.logged_in = True
            print('new account created')
                
        
    def login(self):
        uname = self.uname_entry.get().rstrip()
        pword = self.pword_entry.get().rstrip()
        sha256 = hasher.sha256()
        sha256.update((uname+pword).encode('utf-8'))
        credentials = sha256.hexdigest()
        logged_in = False
        i = 0
        with open(self.file_loc + "usrdata.txt", mode='r') as file:
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
        if not logged_in:
            self.terminal_text["text"] = "INVALID CREDENTIALS"

    def create_user(self):
        print("create account")

    def overwrite_key_confirm(self):
        prompt_overwrite = tk.messagebox.askyesno("Overwrite Existing Key?", "WARNING: \
            THIS CANNOT BE UNDONE AND YOU WILL LOSE ACCESS TO DATA RELATED TO THAT ACCOUNT. \
            CHOOSE NO AND BACK UP IF REQUIRED", icon='warning')
        if prompt_overwrite == 'yes':
            return True
        else:
            return False

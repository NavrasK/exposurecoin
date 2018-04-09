# The GUI for the client

# TODO: Nuke it and start over from the top

import hashlib as hasher
import os
import random
from user_ import User
import tkinter as tk
from tkinter import messagebox

class ClientApp(tk.Frame):
    def __init__(self, master = None):
        self.file_loc = "textfiles/"
        super().__init__(master)
        self.config(width = 500, height = 500)
        self.login_screen()
        self.pack()
        self.user = User()
        self.logged_in = False

    def login_screen(self):
        print("debug")
        self.config(padx=5, pady=5)
        self.title="EXPCoin Client"

        self.prompt = tk.LabelFrame(self, text="Login", padx=5, pady=5, width=200, height=200)
        self.prompt.pack(side="top")
        self.prompt.bind('<Return>', print("enter"))

        self.user_field = (tk.Label(self.prompt, text="Username: "), tk.Entry(self.prompt))
        self.pword_field = (tk.Label(self.prompt, text="Password: "), tk.Entry(self.prompt, show='*'))
        self.create_acc = tk.Button(self.prompt, text="Create a new account", command=self.new_acc_screen)
        self.login_button = tk.Button(self.prompt, text="Login", command=self.login)

        self.user_field[0].grid(row=0, column=0)
        self.user_field[1].grid(row=0, column=1)
        self.pword_field[0].grid(row=1, column=0)
        self.pword_field[1].grid(row=1, column=1)
        self.create_acc.grid(row=3, column=1, pady=2)
        self.login_button.grid(row=2, column=1, pady=2)

    def new_acc_screen(self):
        def validate():
            uname = self.user_field[1].get().rstrip()
            pword = self.pword_field[1].get().rstrip()
            pword_conf = self.conf_pword_field[1].get().rstrip()
            self.user.create(uname, pword, pword_conf)

        self.prompt.config(text="Create Account")
        self.login_button.destroy()
        self.create_acc.config(command=validate, text="Create Account")
        self.conf_pword_field = (tk.Label(self.prompt, text="Confirm Password: "), tk.Entry(self.prompt, show='*'))
        self.conf_pword_field[0].grid(row=2, column=0)
        self.conf_pword_field[1].grid(row=2, column=1)
        self.create_acc.grid(row=3, column=1)
        
    def login(self):
        uname = self.user_field[1].get().rstrip()
        pword = self.pword_field[1].get().rstrip()
        try:
            self.user.login(uname, pword)
        except ValueError:
            messagebox.showerror("Error", "User not found, try again.")
            self.pword_field[1].delete(0, 'end')
            self.user_field[1].delete(0, 'end')
        

    # def overwrite_key_confirm(self):
    #     prompt_overwrite = tk.messagebox.askyesno("Overwrite Existing Key?", "WARNING: \
    #         THIS CANNOT BE UNDONE AND YOU WILL LOSE ACCESS TO DATA RELATED TO THAT ACCOUNT. \
    #         CHOOSE NO AND BACK UP IF REQUIRED", icon='warning')
    #     if prompt_overwrite == 'yes':
    #         return True
    #     else:
    #         return False

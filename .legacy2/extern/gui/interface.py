# The main file that handles the GUI features and layouts

# I need to use user.py in this, I really don't think there's any other way. While a tkinter instance is running, no other code runs. Unless we do the login validation stuff in this directory instead of user, we have figure somehting out. 

import tkinter as tk
# import os

# cur_path = os.path.dirname(__file__)

class GUI(tk.Frame):
    # file_loc = os.path.join(cur_path, '..\\..\\files\\users')
    
    def __init__(self, master):
        super().__init__(master)
        self.title="EXPCoin Client"

        self.config(width = 500, height = 500)
        self.master = master
        self.user = None
        
        self.lg = Login_Window(master)
        self.interface = Interface_Window(master = self.master, user = user)

    def run(self):
        self.lg.mainloop()
        self.user = self.lg.user

        self.interface.user = self.user
        self.interface.mainloop()


class Window(tk.Frame):
    widgets = []
    def __init__(self, master = None):
        super().__init__(master)
    
    def _delete_widg(self, widget):
        self.widgets.remove(widget)
        widget.destroy()

    def close(self):
        for widg in self.widgets:
            widg.destroy()

        self.quit()


class Login_Window(Window):
    def __init__(self, master = None):
        super().__init__(master)
        self.login_screen()

        self.user = None

    def login_screen(self):
        # Screen to log into an exisiting account.  This is the main screen you see on startup

        print("debug")
        self.config(padx=5, pady=5)

        self.prompt = tk.LabelFrame(self, text="Login", padx=5, pady=5, width=200, height=200)
        self.prompt.pack(side="top")
        self.prompt.bind('<Return>', print("enter"))

        self.user_field = (tk.Label(self.prompt, text="Username: "), tk.Entry(self.prompt))
        self.pword_field = (tk.Label(self.prompt, text="Password: "), tk.Entry(self.prompt, show='*'))
        self.create_acc = tk.Button(self.prompt, text="Create a new account", command=self.new_acc_screen)
        self.login_button = tk.Button(self.prompt, text="Login", command=self.login)

        Login_Window.widgets.extend([self.prompt, self.user_field[0], self.user_field[1], self.pword_field[0], self.pword_field[1], self.create_acc, self.login_button])

        self.user_field[0].grid(row=0, column=0)
        self.user_field[1].grid(row=0, column=1)
        self.pword_field[0].grid(row=1, column=0)
        self.pword_field[1].grid(row=1, column=1)
        self.create_acc.grid(row=3, column=1, pady=2)
        self.login_button.grid(row=2, column=1, pady=2)
    
    def new_acc_screen(self):
        # Screen to create a new account

        def validate():
            uname = self.user_field[1].get().rstrip()
            pword = self.pword_field[1].get().rstrip()
            pword_conf = self.conf_pword_field[1].get().rstrip()
            if True:  '''self.user.create(uname, pword, pword_conf):'''
                self.login()

        self._delete_widg(self.login_button)
        self.prompt.config(text="Create Account")
        self.create_acc.config(command=validate, text="Create Account")
        
        self.conf_pword_field = (tk.Label(self.prompt, text="Confirm Password: "), tk.Entry(self.prompt, show='*'))
        Login_Window.widgets.extend(self.conf_pword_field)

        self.conf_pword_field[0].grid(row=2, column=0)
        self.conf_pword_field[1].grid(row=2, column=1)
        self.create_acc.grid(row=3, column=1)

    def login(self):
        uname = self.user_field[1].get().rstrip()
        pword = self.pword_field[1].get().rstrip()

        try:
            # self.user.login(uname, pword)
            self.close()
        except ValueError:
            messagebox.showerror("Error", "User not found, try again.")
            self.pword_field[1].delete(0, 'end')
            self.user_field[1].delete(0, 'end')

    def close(self):
        super().close()
        return self.user


class Interface_Window(Window):
    def __init__(self, master = None, user = None):
        super().__init__(master)
        self._init_menubar()
        self.pack()
        self.master = master
        print("interface")
        self.user = user
    
    def _init_menubar(self):
        self.menubar = tk.Menu(self)
        Interface_Window.widgets.append(self.menubar)

        acc_menu = tk.Menu(self.menubar, tearoff=0)
        acc_menu.add_command(label="My Account", command=self.display_Account)
        acc_menu.add_command(label="Logout", command=self.logout)

        help_menu = tk.Menu(self.menubar, tearoff=0)
        help_menu.add_command(label="Help", command=self.display_Help)
        help_menu.add_command(label="About", command=self.display_About)

        self.menubar.add_cascade(label="Account", menu=acc_menu)
        self.menubar.add_cascade(label="Help", menu=help_menu)

        self.master.config(menu=self.menubar)
    
    def display_Account(self):
        self.acc_Frame = tk.LabelFrame(self, text='test')
        self.acc_Frame.pack(side='top')
        Interface_Window.widgets.append(self.acc_Frame)
        # line = 'test'
        test_line = tk.StringVar()
        test_line.set('test')
        # accounts = tk.StringVar(master=self.acc_Frame, value="User ID: " + self.user.userID + "\n Local Balance: ONE MILLION DOLLARS")
        # accounts.set"User ID: " + self.user.userID + "\n Local Balance: ONE MILLION DOLLARS")

        self.acc_info = tk.Label(self, textvariable=test_line)

    def logout(self):
        pass
    
    def display_About(self):
        pass

    def display_Help(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()

    app = GUI(root)

    GUI.run()
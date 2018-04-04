from tkinter import *

class ClientApp(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.clicks = 0
        self.add_elements()

    def add_elements(self):
        self.testbutton = Button(self, text="TEST")
        self.testbutton["command"] = self.update_clicks
        self.testbutton.grid()
        self.testlabel = Label(self, text=str(self.clicks))
        self.testlabel.grid()

    def update_clicks(self):
        self.clicks += 1
        self.testlabel["text"] = self.clicks

root = Tk()
root.title("TEST WINDOW")
root.geometry("500x400")

app = ClientApp(root)

root.mainloop()
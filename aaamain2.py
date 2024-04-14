# Weather Data Analysis Program
import tkinter as tk
from tkinter import *
from tkinter import messagebox

import data_create_acct

class DataGUI:
    def __init__(self):
#Create the main window
        self.main_win=tk.Tk()
        self.main_win.title(" D a t a    A n a l y s i s    P r o g r a m ")
#set the main win size
        self.main_win.minsize(width=900,height=500)
#config columns and rows of main_win
        for c in range(9):
            self.main_win.columnconfigure(c, minsize=100)
        for r in range(9):
            self.main_win.rowconfigure(r, minsize=50)
#Creation of heading_label w/ position and grid (row, column)
        self.heading_label = tk.Label(text= ' Data Analysis Program ',\
                                      font=("fixedsys",16), fg="green")
        self.heading_label.grid(row=1, column=3, columnspan=3, rowspan=3, sticky=N)
#Button control- login_button w/ params
        self.login_button = tk.Button(text=' Login ', font=("Helvetica",10),\
                                      command= print('LOGIN BUTTON'))
        self.login_button.grid(row=8,column=2)
#Button control- create_acct w/ params
        self.create_acct_button = tk.Button(text=' Create Account ', font=("Helvetica",10),\
                                            command= self.create_account)
        self.create_acct_button.grid(row=8,column=4)
#Button control- quit_button w/ params
        self.quit_button = tk.Button(text=' Cancel ', font=("Helvetica",10),\
                                     command= self.main_win.destroy)
        self.quit_button.grid(row=8,column=6)
#Enter the tkinter main loop
        tk.mainloop()
#function to create the account creation window(code in another file)
def create_account(self):
#create the window... this code is located in the file data_create_acct.py
    CreateAcctWin= data_create_acct.AccountGUI()
#forces a wait until the 2nd window is closed
    CreateAcctWin.account_win.wait_window()
#disables create button on main win
    self.create_acct_button.config(state=DISABLED)
#enables login
    self.login_button.config(state=NORMAL)
#create an instance of the class
dataAnalysis = DataGUI()

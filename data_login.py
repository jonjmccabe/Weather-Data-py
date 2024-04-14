#contains login function

from tkinter import*
from tkinter import messagebox
import tkinter as tk

#modify the main window to accept the login password
def login(self):

#destroy the buttons and title
    self.heading_label.destroy()
    self.login_button.destroy()
    self.create_acct_button.destroy()
    self.quit_button.destroy()
    #destory DAP GIF

#new columns and rows for login layout
    for r in range(29):
        self.main_win.rowconfigure(r, minsize=0)
    for c in range(6):
        self.main_win.columnconfigure(c, minsize=0)
    for r in range(12):
        self.main_win.rowconfigure(r, minsize=20)
    for c in range(6):
        self.main_win.columnconfigure(c, minsize=60)

#Create widgets for login layout (entry, headling, labels etc.)
#heading
    self.heading_label_login_main = tk.Label(text='Account login',\
                                             justify='left',font=("fixedsys",10))
    self.heading_label_login_main.grid(row=1, column=1, columnspan=4, sticky=W)


    self.instruct_label = tk.Label(text= 'Enter the Username and Password associated with your DAP account',\
                                                   font=("fixedsys",10))
    self.instruct_label.grid(row=4, column=2, columnspan= 5)


    self.instruct_label_two = tk.Label(text='tab key to change entry box',\
                                             justify='left',font=("fixedsys",10))
    self.instruct_label_two.grid(row=9, column=4, columnspan=4, sticky=W)


    self.instruct_label_three = tk.Label(text='return key once credentials are entered',\
                                             justify='left',font=("fixedsys",10))
    self.instruct_label_three.grid(row=11, column=4, columnspan=4, sticky=W)
#UN
    self.userName_label = tk.Label(text='Username:',\
                                   justify='left',font=("fixedsys",10))
    self.userName_label.grid(row=8, column=2, columnspan=2, sticky=W)
    self.user_entry = tk.Entry(width = 18, justify='left', font=("fixedsys",10))
    self.user_entry.grid(row= 8, column=4, columnspan=2, sticky=W, padx=10 )
    self.user_entry.focus_force()

#PW
    self.password_label = tk.Label(text='Password:',\
                                   justify='left',font=("fixedsys",10))
    self.password_label.grid(row=10, column=2, columnspan=4, sticky=W)
    self.password_entry = tk.Entry(width = 18, justify='left', font=("fixedsys",10))
    self.password_entry.grid(row= 10, column=4, columnspan=2, sticky=W, padx=10)
    self.password_entry.bind('<Return>', self.verify_account)
#Buttons

    

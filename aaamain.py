# Weather Data Analysis Program

import data_create_acct_gui

from tkinter import*
from tkinter import messagebox
import tkinter as tk


class DataGUI:
    def __init__(self):
#Create the main window
        self.main_win=tk.Tk()
        self.main_win.title(" D a t a    A n a l y s i s    P r o g r a m ")
#set the main_win size
        self.main_win.minsize(width=900,height=600)
#config columns and rows of main_win
        for c in range(9):
            self.main_win.columnconfigure(c, minsize=100)
        for r in range(9):
            self.main_win.rowconfigure(r, minsize=50)
#Heading_label w/ position and grid (row, column)
        self.heading_label = tk.Label(text= '  Data  Analysis  Program ',\
                                      font=("fixedsys",16), fg="green")
        self.heading_label.grid(row=1, column=3, columnspan=3, rowspan=3, sticky=N)
#Button control- login_button w/ params
        self.login_button = tk.Button(text=' Login ', width=16, font=("Helvetica",10),\
                                      command= print('LOGIN BUTTON'))
        self.login_button.grid(row=9,column=2)
#Button control- create_acct w/ params
        self.create_acct_button = tk.Button(text=' Create Account ', width=16,\
                                            font=("Helvetica",10),\
                                            command= self.create_account)
        self.create_acct_button.grid(row=9,column=4)
#Button control- quit_button w/ params
        self.quit_button = tk.Button(text=' Cancel ', width=16, font=("Helvetica",10),\
                                     command= self.main_win.destroy)
        self.quit_button.grid(row=9,column=6)
#photo
        photo = PhotoImage(file= "DAP.gif")
        self.labelGIF = tk.Label(image= photo)
        self.labelGIF.image = photo # retain a reference
        self.labelGIF.grid(row = 2, column = 2, columnspan=6, rowspan=24, sticky=NW, padx=50)
#freeze main_win size
        self.main_win.resizable(height=False, width=False)
#Enter the tkinter main loop
        tk.mainloop()






    def create_account(self):
#Test
        print('Inside create_account function in main')
#Instantiation
        CreateAcctWin = data_create_acct_gui.AccountGUI()
#window wait
        CreateAcctWin.acct_win.wait_window()
#state of button control (login)
        self.login_button.config(state = NORMAL)



#    def call_login(self):
#       self.labelGIF.destroy()
#       data_login.login(self)




#create an instance of the class
dataAnalysis = DataGUI()

# Weather Data Analysis Program

import data_create_acct_gui
import data_login

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
                                      command= self.call_login)
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

#call login
    def call_login(self):
       self.labelGIF.destroy()
       data_login.login(self)

#verify acct algorithm
    def verify_account(self,event):
        print('Now in verify>>>>>>>>>..')
        validUser = False
        validPassword = False
        counter = 0
        slot = 0
#Get entry from user
        userName = self.user_entry.get()
        userPassword =self.password_entry.get()
#if userName != '' and userPassword != '':
        try:
            userNameFile = open('acct_user_names.txt', 'r')
#loop line by line to check the values
            for userTemp in userNameFile:
                print('userTemp is ' + userTemp + ' and userName is ' + userName)
                print('slot is now ' + str(slot) + ' and counter is ' + str(counter))
                if userName == userTemp.rstrip():
                    validUser = True
                    slot = counter
                else:
                    counter = counter + 1

            print('AFTER loop slot is now ' + str(slot) + ' and counter is ' + str(counter))
            userNameFile.close()

            print('valid user is now ' + str(validUser))
#if it exists in the file
            if (validUser == True):
#open the file for reading
                print('checking PW')
                passwordFile = open('acct_user_password.txt', 'r')
#declare outside loop
                filePassword = ''
#read up to the (but not including...
                for x in range(slot +1):
                    filePassword = passwordFile.readline()
                    print('\n filePassword is now ' + filePassword)

                passwordFile.close()

                if userPassword == filePassword.rstrip():
                    validPassword = True
                    print('\n THE PASSWORD MATCHES ')

            if validUser == True and validPassword == True:
                tk.messagebox.showinfo('Authentication Successful', 'Login Successful')
                self.show_main()
            else:
                tk.messagebox.showinfo('Invalid Account Credentials', 'Account does not match our records')

        except IOError:
            print('No File exists.')

#call by
    def show_main (self):
        print('In show_main now.')
#destroy login controls for main main
        self.heading_label_login_main.destroy()
        self.instruct_label.destroy()
        self.instruct_label_two.destroy()
        self.instruct_label_three.destroy()
        self.userName_label.destroy()
        self.user_entry.destroy()
        self.password_label.destroy()
        self.password_entry.destroy()
        self.instruct_label.destroy()

        for c in range(29):
            self.main_win.columnconfigure(c, minsize=15)
        for r in range(18):
            self.main_win.rowconfigure(r, minsize=40)

#morph main_win to program interface
        self.main_win.minsize(width=1200,height=500)
        
        self.heading_label = tk.Label(text= ' Weather Data Analytical Interface',\
                                      font=("fixedsys",26), fg="green")
        self.heading_label.grid(row=1, column=13, columnspan=5, rowspan=3, sticky=N)
#Interface photo 
        photofb = PhotoImage(file= "DAPfb.gif")
        self.labelGIFfb = tk.Label(image= photofb)
        self.labelGIFfb.image = photofb # retain a reference
        self.labelGIFfb.grid(row = 1, column = 1, columnspan=6, rowspan=18, sticky=N, padx=10)




#store radio button selection
        self.radio_var = tk.StringVar()
#default radio selected
        self.radio_var.set('1')

#Barometric pressure and temperature radio button
        self.baroTemp = tk.Radiobutton(text="Barometric pressure and temperature",\
                                            font=("Helvetica",14), variable=self.radio_var, value='1')
        self.baroTemp.grid(padx=20,row = 4, rowspan = 3, column = 10, columnspan =7, stick=W)
#Barometric pressure and windspeed radio button
        self.baroWindSpd = tk.Radiobutton(text="Barometric pressure and windspeed",\
                                            font=("Helvetica",14), variable=self.radio_var, value='2')
        self.baroWindSpd.grid(padx=20,row = 5, rowspan = 3, column = 10, columnspan =7, stick=W)
#Barometric pressure and sky cover radio button
        self.baroSkyCvr = tk.Radiobutton(text="Barometric pressure and sky cover",\
                                            font=("Helvetica",14), variable=self.radio_var, value='3')
        self.baroSkyCvr.grid(padx=20,row = 6, rowspan = 3, column = 10, columnspan =7, stick=W)
#Barometric pressure and temperature radio button
        self.tempDewPt = tk.Radiobutton(text="Temperature and dew point",\
                                            font=("Helvetica",14), variable=self.radio_var, value='4')
        self.tempDewPt.grid(padx=20,row = 7, rowspan = 3, column = 10, columnspan =7, stick=W)





#Listbox start and end year configuration
        self.startYear_var = StringVar()
        self.endYear_var = StringVar()
#range of years
        self.choices = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
        self.choices_var = StringVar(value=self.choices)
        self.choices_var.set(self.choices)
#set default option for start and end years
        self.startYear_var.set('2010')
        self.endYear_var.set('2018') 
#Listbox control- start year
        self.startYearLB = tk.Listbox(listvariable=self.choices_var)
        self.startYearLB.grid(padx=20,row = 11, rowspan = 3, column = 9, columnspan =7, stick=W)
#Listbox control- end year
        self.endYearLB = tk.Listbox(listvariable=self.choices_var)
        self.endYearLB.grid(padx=20,row = 11, rowspan = 3, column = 14, columnspan =7, stick=W)

#startYear Listbox label
        self.startY_label = tk.Label(text= '    Start Year',\
                                      font=("fixedsys",14), fg="green")
        self.startY_label.grid(row=10, column=9, columnspan=3, rowspan=2, sticky=NE)
#endYear Listbox label
        self.endY_label = tk.Label(text= 'End Year',\
                                      font=("fixedsys",14), fg="green")
        self.endY_label.grid(row=10, column=12, columnspan=3, rowspan=2, sticky=NE)



#Button control- display data
        self.display_data_button = tk.Button(text=' Display Data ', width=18,\
                                            font=("Helvetica",12),\
                                            command= self.data_extract_func)
        self.display_data_button.grid(row=14, rowspan= 3, column=12, columnspan= 3, stick=W)




#def data extraction func
    def data_extract_func(self):
        print('Button selectied is ' + str(self.radio_var.get()))

        mylines = []
        with open ('my_test_data.txt', 'rt') as myfile:
            for myline in myfile:
                mylines.append(myline.rstrip('\n'))
            for element in mylines:
                print(element)
                print(element.find("2010",14, 17))








'''

#exception handling
        try:
#opens weather_data_set.txt
            my_data_set = open('weather_data_set.txt', 'r')

			...

# output if the file cannot be opened
	except IOError:
	    print('No File exists.')
# output if the data type is incorrect
	except ValueError:
	    print(‘A bad value was read’)
# default handler
	except:
	    print(‘Error in program.’)
#remembers to close file
	finally:
	    weather_data_set.close()
'''

        

              




#create an instance of the class
dataAnalysis = DataGUI()

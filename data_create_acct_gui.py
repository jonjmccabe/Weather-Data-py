# acct file of WDAP, UN and PW setup with validation

from tkinter import*
from tkinter import messagebox
import tkinter as tk


class AccountGUI:

#self recieved as acct
    def __init__(acct):

#Test
        print('In the init for AccountGUI')

#create acct window w/ title
        acct.acct_win=tk.Tk()
        acct.acct_win.title(" A c c o u n t   C r e a t i o n")

#set window size w/ row and column params
        acct.acct_win.minsize(width=750,height=325)
        for c in range(12):
            acct.acct_win.columnconfigure(c, minsize=50)
        for r in range(10):
            acct.acct_win.rowconfigure(r, minsize=50)



#Account creation label
        acct.acct_win.acct_create_label= tk.Label(acct.acct_win, text='Create an account',\
                                             font=("fixedsys",10), fg="green")
        acct.acct_win.acct_create_label.grid(row=1,column=1)
#UN label
        acct.acct_win.un_label= tk.Label(acct.acct_win, text='Username:',\
                                             font=("fixedsys",10), fg="green")
        acct.acct_win.un_label.grid(row=2,column=3)
#UN entry
        acct.acct_win.un_entry= tk.Entry(acct.acct_win, width= 15, justify='left',\
                                         font=("Helvetica",10))
        acct.acct_win.un_entry.grid(row=2, column= 4, stick=W)
#UN entry focus force
        acct.acct_win.un_entry.focus_force()
#PW label
        acct.acct_win.pw_label= tk.Label(acct.acct_win, text='Password:',\
                                             font=("fixedsys",10), fg="green")
        acct.acct_win.pw_label.grid(row=4,column=3)
#PW entry
        acct.acct_win.pw_entry= tk.Entry(acct.acct_win, width= 15, justify='left',\
                                         font=("Helvetica",10), show='*')
        acct.acct_win.pw_entry.grid(row=4, column= 4, stick=W)
#Button control- quit_button w/ params
        acct.acct_win.acctcre_cancel_button= tk.Button(acct.acct_win, text=' Cancel ', width=10,\
                                               font=("Helvetica",10), command= acct.acct_win.destroy)
        acct.acct_win.acctcre_cancel_button.grid(row=7, column=4, sticky=W)
#Button control- CA_button w/ params
        acct.acct_win.make_acct_button= tk.Button(acct.acct_win, text=' Create this Account ', width=16 ,\
                                               font=("Helvetica",10), command= acct.verify_new_user)
#acct.messbox func below lambda
        acct.acct_win.make_acct_button.grid(row=6, column=4, sticky=W)
#lift this win to top
        acct.acct_win.lift()


#Function that verifies new user's Username ( un ) credentials against existing user creds.
    def verify_new_user(acct):
        valid = True
#get new username from un_entry widget
        newUser = (acct.acct_win.un_entry.get())
        print ('newUser is: ' + newUser + '\n')
        try:
#try opening the file to read
            userDataFile = open('acct_user_names.txt', 'r')
# loop line by line to check the values
            for userTemp in userDataFile:
                print('userTemp from file is: ' + userTemp)
                if newUser == userTemp.rstrip():
                    valid = False

            userDataFile.close()
#if name exists in the file
            if (valid == False):
                tk.messagebox.showinfo('Invalid username', ' That username already exists.')
                acct.acct_win.un_entry.delete(0,END)
                acct.acct_win.un_entry.focus_force()
                acct.acct_win.lift()
#not in the file...call verify and pass it the username to write if pass is good
            else:
                acct.verify_new_pass(newUser)

        except IOError:
            print('No File exists.')




    def verify_new_pass(acct, newUser):
        valid = False
#get the new password from pw_entry widget
        newPassw = (acct.acct_win.pw_entry.get())
        print ('Getting password ' + newPassw)

#call to verify password criteria is met
        if acct.verify_pass(newPassw):
#open the user file to append it w/ new user
            userFile = open('acct_user_names.txt', 'a')
            userFile.write(newUser + '\n')
            userFile.close()

#open the password file to append it
            passwordFile = open('acct_user_password.txt', 'a')
#add the new password to the file with a newline
            passwordFile.write(newPassw + '\n')
            passwordFile.close()
            tk.messagebox.showinfo('Account Creation','Account Successfully Created.')
            acct.acct_win.lift()
            acct.acct_win.destroy()
        else:
            tk.messagebox.showerror('Password Validation', '"' + newPasw + '"' + ' is not a valid password.')
            acct.acct_win.lift()
#clear password txt
            acct.acct_win.pw_entry.delete(0,END)
            acct.acct_win.focus_force()
#give pw_entry the focus
            acct.acct_win.pw_entry.focus_force()




#walk the string to validate (ref page 425)
    def verify_pass(acct, newPassw):

        isValid = False
        longEnough = False
        hasUpper = False
        hasLower = False
        hasDigit = False

        if len(newPassw) >= 9:
            longEnough = True

            for ch in newPassw:
                if ch.isupper():
                    hasUpper = True
                if ch.islower():
                    hasLower = True
                if ch.isdigit():
                    hasDigit = True

        if longEnough and hasUpper and hasLower and hasDigit:
            isValid = True

        return isValid













    def messbox(acct):
        tk.messagebox.showinfo('Info Box Demo', 'The account was created.')

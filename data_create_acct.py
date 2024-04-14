acct.account_win=tk.Tk()
acct.account_win.title(" Account Creation ")
acct.account_win.userName_entry = tkinter.Entry(acct.account_win, \
                                                  width = 15, justify='right', font= ("Helvetica",10))
acct.account_win.userName_entry.grid(row=2, column=4, sticky=W)
acct.account_win.userName_entry.focus_force()

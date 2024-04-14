from tkinter import*
import tkinter as tk

class DataGUI:
    def __init__(self):
        self.main_win=tk.Tk()
        self.main_win.title("Data Analysis Program")
        self.main_win.minsize(width=500,height=500)
        self.main_win.columnconfigure(0, minsize =40)
        self.main_win.columnconfigure(1, minsize =100)
        self.main_win.columnconfigure(2, minsize =50)
        self.main_win.rowconfigure(0, minsize =50)
        self.main_win.rowconfigure(1, minsize =50)
        self.main_win.rowconfigure(2, minsize =50)
        self.heading_label = tk.Label(text='Data Analysis Program',\
                                      font=("Helvectica",16), fg="blue")
        self.heading_label.grid(row=1, column=2,columnspan=5,rowspan=5)
        self.quit_button.minsize(width=20,height=10)
        self.quit_button.columnconfigure(0, minsize =40)
        self.quit_button.columnconfigure(1, minsize =100)
        self.quit_button.columnconfigure(2, minsize =50)
        self.quit_button.rowconfigure(0, minsize =50)
        self.quit_button.rowconfigure(1, minsize =50)
        self.quit_button.rowconfigure(2, minsize =50)
        self.quit_button=tk.Button(text=' Cancel ',width=16,\
                                    font=("Helvetica",10),relief=raised,\
                                    fg="blue",\
                                    command=self.main_window.destory)
        self.quit_button.grid(row=2, column=2, columnspan=1, rowspan= 1, padx=1)
        tk.mainloop()
dataAnalysis = DataGUI()
    

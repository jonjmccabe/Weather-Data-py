import tkinter as tk
from tkinter import messagebox

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
        tk.mainloop()
dataAnalysis = DataGUI()
    

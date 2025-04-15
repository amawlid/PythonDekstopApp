from tkinter import *
from tkinter import ttk 
from datetime import datetime 

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text="Stop", command=root.destroy).grid(column=0,row=0)
x = datetime.today().strftime("%Y-%m-%d") 
ttk.Label(frm, text= x).grid(column=0,row=1)

root.mainloop()

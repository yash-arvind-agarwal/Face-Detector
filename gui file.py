from tkinter import*
from test import *
from train import *
import tkinter as tk
root=tk.Tk()
label=Label(root,text="Face Recognizer",bg="grey",width=100,border=10,).pack()
button_1=tk.Button(root,text="test",fg="red",bg="GREEN",width=10,padx=3,command=lambda:test()).pack(side=LEFT)
button_2=tk.Button(root,text="train",fg="black",bg="Red",width=10,padx=3,command=lambda:train()).pack(side=RIGHT)
button_3=tk.Button(root,text="quit",fg="Red",width=10,padx=3,command=root.destroy).pack(side=RIGHT)
root.mainloop()
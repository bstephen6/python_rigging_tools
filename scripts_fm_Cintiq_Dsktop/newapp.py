from distutils.core import setup, sys
import tkinter, tkinter.constants
from tkinter import *

window = Tk()
window.title("new app")
window.geometry("500x500")

labelText = "go to unreal engine window"

Button(window, text=labelText, height = 5).grid(row=1,column =1, columnspan=1)
Spinbox(window, from_=0.0, to=1.0, increment= .05 ).grid(row=2,column=1, columnspan = 1)



window.mainloop()
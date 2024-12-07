import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
#window
window = tk.Tk()
window.title("Employee Registration")
window.geometry('1520x900')

#frame for the employee basic information

frame1 = Frame(window, width=1100, height=160, border=0, bg='light gray')
frame1.place(x=200, y=220)
#frame for the basic employee information
frame2 = Frame(window, width=1100, height=160, border=0, bg='light gray')
frame2.place(x=200, y=390)


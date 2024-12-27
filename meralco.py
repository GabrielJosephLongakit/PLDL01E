import tkinter as tk
from threading import main_thread
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Meralco Form")
window.geometry('1000x800')

class design_gui_interface():
    def __int__(self, frame1):
        frame1 = ''

    def create_frame(self):
        self.frame1 = Frame(window, width=700, height=800, border=0)
        self.frame1.place(relx=0.5, rely=0.1, anchor=N)

    def heading_design(self, text_value):
        heading = Label(self.frame1, text=text_value, fg='black', font=('Arial', 15, 'bold'))
        heading.pack(pady=5)

    def applicationform(self, text_value):
        heading = Label(self.frame1, text=text_value, fg='black', font=('Arial', 15, 'bold'))
        heading.pack(pady=5)

    def image_design(self, image_location, x, y, length, width):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.lbl = Label(window, image=self.bck_pic)
        self.lbl.place(x=x, y=y)

# Create GUI design instance
my_gui_design = design_gui_interface()
my_gui_design.create_frame()
my_gui_design.heading_design('ACCREDITED MERALCO CONTRACTORS (AMC)')
my_gui_design.applicationform('APPLICATION FORM')
uploaded_image = my_gui_design.image_design(r'C:\Users\longa\PycharmProjects\PLDL01E\meralco_yan_sha.png', 75, 70, 177, 148)

window.mainloop()
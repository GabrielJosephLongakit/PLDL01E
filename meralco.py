import tkinter as tk
from io import text_encoding
from threading import main_thread
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk


# Window
window = tk.Tk()
window.title("Meralco Form")
window.geometry('1300x800')

var = IntVar()

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

    def label_design(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, font=('Arial', 14, 'bold'))
        self.lbl.place(x=x, y=y)

    def subtext_design(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text = text_value, font=('Arial', 12))
        self.lbl.place(x=x,y=y)

    def label_design2(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, font=('Arial', 13, 'bold'))
        self.lbl.place(x=x, y=y)

    def textbox_design1(self, x, y):
        self.textbox = Text(width=25, height=1, fg='black', bg='white', font=('Arial', 11, 'bold'))
        self.textbox.place(x=x, y=y)

    def subtext_design2(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, font=('Arial', 10))
        self.lbl.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=20, height=1, fg='black', bg='white', font=('Arial', 11, 'bold'))
        self.textbox.place(x=x, y=y)

    def checkbox(self, x, y):
        self.checkbox = Checkbutton(window, text="Single Proprietorship", variable=var, font=('Arial', 11))
        self.checkbox.place(x=x, y=y)

    def checkbox2(self, x, y):
        self.checkbox = Checkbutton(window, text="Partnership", variable=var, font=('Arial', 11))
        self.checkbox.place(x=x, y=y)

    def checkbox3(self, x, y):
        self.checkbox = Checkbutton(window, text="Corporation", variable=var, font=('Arial', 11))
        self.checkbox.place(x=x, y=y)

    def checkbox4(self, x, y):
        self.checkbox = Checkbutton(window, text="Cooperative", variable=var, font=('Arial', 11))
        self.checkbox.place(x=x, y=y)

    def checkbox5(self, x, y):
        self.checkbox = Checkbutton(window, text="Institute of Integrated Electrical Engineers (IIEE)", variable=var, font=('Arial', 11))
        self.checkbox.place(x=x, y=y)

    def checkbox6(self, x, y):
        self.checkbox = Checkbutton(window, text="Society of Philippine Electrotechnical Constructors and Suppliers Inc. (SPECS)", variable=var, font=('Arial', 11))
        self.checkbox.place(x=x, y=y)

    def image_design2(self, image_location, x, y, length, width):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)
        self.bck_pic2 = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.lbl = Label(window, image=self.bck_pic2)
        self.lbl.place(x=x, y=y)

# Create GUI design instance
my_gui_design = design_gui_interface()
my_gui_design.create_frame()
my_gui_design.heading_design('ACCREDITED MERALCO CONTRACTORS (AMC)')
my_gui_design.applicationform('APPLICATION FORM')
my_gui_design.image_design(r'C:\Users\longa\PycharmProjects\PLDL01E\meralco_yan_sha.png', 100, 70, 177, 148)
my_gui_design.label_design(200, 250, 'APPLICATION INFORMATION')
my_gui_design.subtext_design(200, 279, 'Business Name')
my_gui_design.subtext_design(200, 300, 'Office Address')
my_gui_design.subtext_design(200, 340, 'Contact Information')
my_gui_design.label_design2(200, 400, 'REPRESENTATIVE INFORMATION')
my_gui_design.subtext_design(200, 450, 'Official Representatives')
my_gui_design.subtext_design(200, 500, 'Official Representatives')
my_gui_design.subtext_design(200, 540, 'Affiliation')
my_gui_design.textbox_design1(400, 279)
my_gui_design.textbox_design1(400, 300)
my_gui_design.subtext_design2(410, 327, 'Landline No.')
my_gui_design.textbox_design2(410, 350)
my_gui_design.subtext_design2(650, 327, 'Fax No.')
my_gui_design.textbox_design2(650, 350)
my_gui_design.subtext_design2(900, 327, 'E-mail Address')
my_gui_design.textbox_design2(900, 350)
my_gui_design.subtext_design2(410, 427, 'Name-Position')
my_gui_design.textbox_design2(410, 450)
my_gui_design.textbox_design2(410, 470)
my_gui_design.subtext_design2(600, 427, 'Landline or Mobile No.')
my_gui_design.textbox_design2(600, 450)
my_gui_design.textbox_design2(600, 470)
my_gui_design.subtext_design2(800, 427, 'Fax no.')
my_gui_design.textbox_design2(800, 450)
my_gui_design.textbox_design2(800, 470)
my_gui_design.subtext_design2(1000, 427, 'E-mail Address')
my_gui_design.textbox_design2(1000, 450)
my_gui_design.textbox_design2(1000, 470)
my_gui_design.checkbox(410, 500)
my_gui_design.checkbox2(600, 500)
my_gui_design.checkbox3(800, 500)
my_gui_design.checkbox4(1000, 500)
my_gui_design.checkbox5(410, 540)
my_gui_design.checkbox6(410, 570)
my_gui_design.image_design2(r'C:\Users\longa\PycharmProjects\PLDL01E\meralco_contractors.png', 1000, 70, 177, 148)
window.mainloop()
import tkinter as tk
from threading import main_thread
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
#window
window = tk.Tk()
window.title("Employee Registration")
window.geometry('1520x900')

class design_gui_inteface():
    def __int__(self, frame1):
        frame1 = ''

    def frames(self, x, y):
        self.frame1 = Frame(window, width=1100, height=160, border=0)

        self.frame1.place(x=x, y=y)

    def heading_design(self, x, y, text_value):
        self.text_value = text_value
        self.heading = Label(text=text_value, fg='black', font=('Times New Roman', 30, 'bold'))
        self.heading.place(x=x, y=y)

    def subheading_design(self, x, y, text_value):
        self.text_value = text_value
        self.subheading = Label(text=text_value, fg='black', font=('Times New Roman', 25, 'bold'))
        self.subheading.place(x=x, y=y)

    def eaf_design(self, x, y, text_value):
        self.text_value = text_value
        self.eaf_design = Label(text=text_value, fg='black', font=('Times New Roman', 20, 'bold'))
        self.eaf_design.place(x=x, y=y)

    def textbox_design1(self, x, y):
        self.textbox = Text(width=25, height=1, fg='black', bg='white', font=('Times New Roman', 11, 'bold'))
        self.textbox.place(x=x, y=y)

    def label_design(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, font=('Times New Roman', 10))
        self.lbl.place(x=x, y=y)

    def combo_field(self, x, y, combo_values):
        self.n = tk.StringVar()
        self.combo_fields = ttk.Combobox(window, width=55, textvariable=self.n)
        self.combo_fields['values'] = combo_values
        self.combo_fields.place(x=x, y=y)
        self.combo_fields.current()

    def class_sched(self, x, y, text_value):
        self.text_value = text_value
        self.class_sched = Label(text=text_value, fg='black', font=('Times New Roman', 15, 'bold'))
        self.class_sched.place(x=x, y=y)

    def course_description(self, x, y, text_value):
        self.text_value = text_value
        self.course_description = Label(text=text_value, fg='black', font=('Times New Roman', 15, 'bold'))
        self.course_description.place(x=x,y=y)

    def units(self, x, y, text_value):
        self.text_value = text_value
        self.units = Label(text=text_value, fg='black', font=('Times New Roman', 15, 'bold'))
        self.units.place(x=x,y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=40, height=1, fg='black', bg='white', font=('Times New Roman', 11, 'bold'))
        self.textbox.place(x=x, y=y)


my_gui_design = design_gui_inteface()
my_gui_design.heading_design(400, 20, 'Lyceum of the Philippines University')
my_gui_design.subheading_design(540, 80, '2nd Semester,AY 2024-2025')
my_gui_design.eaf_design(550, 120, 'Enrollment Assessment Form')
student_no = my_gui_design.textbox_design1(440, 225)
student_no_lbl = my_gui_design.label_design(440, 200, 'STUDENT NUMBER')
name = my_gui_design.textbox_design1(440, 275)
namelbl = my_gui_design.label_design(440, 250, 'NAME')
coursetxt = my_gui_design.textbox_design1(858, 225)
courselbl = my_gui_design.label_design(858, 200, 'COURSE')
collegelbl = my_gui_design.label_design(858, 250, 'COLLEGE')
college = my_gui_design.combo_field(858, 275, ('College of Engineering, Computer Studies, and Architecture', 'College of Fine Arts and Design', 'College of International Tourism and Hospitality Management', 'College of Business and Administration', 'College of Liberal Arts and Education', 'College of Allied Medical Sciences', 'College of Nursing'))
my_gui_design.class_sched(440, 320, 'SUBJECT CODE')
my_gui_design.course_description(650, 320, 'COURSE DESCRIPTION')
my_gui_design.units(1000, 320, 'UNITS')
subjcodecombo = my_gui_design.textbox_design1(440, 360)
subjcodecombo2 = my_gui_design.textbox_design1(440, 390)
subjcodecombo3 = my_gui_design.textbox_design1(440, 420)
coursedesc = my_gui_design.textbox_design2(660, 360)
coursedesc2 = my_gui_design.textbox_design2(660, 390)
coursedesc3 = my_gui_design.textbox_design2(660, 420)
units = my_gui_design.textbox_design1(1000, 360)
units2 = my_gui_design.textbox_design1(1000, 390)
units3 = my_gui_design.textbox_design1(1000, 420)
window.mainloop()
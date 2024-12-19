import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

#window
window = tk.Tk()
window.title("Employee Registration")
window.geometry('1000x1400')

class design_gui_interface():
    def __int__(self,frame1):
        frame1 = ''
    def frames(self,x,y):
        self.frame1 = Frame(window, width=1100, height=160, border=0, bg='light gray')
        self.frame1.place(x=x, y=y)

    def heading_design(self, x, y, text_value):
        self.text_value = text_value
        self.heading = Label(text=text_value, fg='black', font=('Algerian', 30, 'bold'))
        self.heading.place(x=x,y=y)

    def textbox_design1(self, x, y):
        self.textbox = Text(width=25, height=1, fg='black', bg='white', font=('Arial', 11, 'bold'))
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=31, height=1, fg='black', bg='white', font=('Arial', 11, 'bold'))
        self.textbox.place(x=x, y=y)

    def label_design(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, bg='light gray', font=('Calibre', 10))
        self.lbl.place(x=x, y=y)

    def button_design(self, x, y, text_value, width_value, bg_value):
        self.bg_value = bg_value
        self.width_value = width_value
        self.text_value = text_value
        self.upload_button = Button(width=width_value, pady=7, text=text_value, bg=bg_value, fg='white', cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

    def image_design(self, image_location, x, y, length, width):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.lbl = Label(window, image=self.bck_pic)
        self.lbl.place(x=x, y=y)

    def combo_field(self, x, y, combo_values):
        self.n = tk.StringVar()
        self.combo_fields = ttk.Combobox(window, width=30, textvariable=self.n)
        self.combo_fields['values'] = combo_values
        self.combo_fields.place(x=x, y=y)
        self.combo_fields.current()

# Adding combobox drop down list
#combo_field['values'] = (' Female', ' Male ', ' Unidentified')
#combo_field.place(x=649, y=330)

# Adding combox for civil status
# Combobox creation
#n = tk.StringVar()
#combo_field1 = ttk.Combobox(window, width=30, textvariable = n)
#combo_field1['values'] = (' Single', ' Married ', ' Widow', ' Legally Separated', ' Annulled')
#combo_field1.place(x=858, y=330)
#combo_field1.current()
#displaying the frames create
#instantiation of the class
my_gui_design = design_gui_interface()
#call frames attribute within the class named as design_gui_interface
#call for frame 1
my_gui_design.heading_design(400, 20, 'PEGASUS Employee Registration Form')
my_gui_design.frames(200, 220)
#call for frame 2
my_gui_design.frames(200, 390)
#call for frame 3
my_gui_design.frames(200, 560)
# calls for the combo
combo_gender = my_gui_design.combo_field(649, 330, ('Female', ' Male', 'Unidentified'))
combo_civil_status = my_gui_design.combo_field(858, 330,(' Single', ' Married ', ' Widow', ' Legally Separated', ' Annulled'))
#text box in first frame
firstnametxt = my_gui_design.textbox_design1(440, 262)
middle_nametxt = my_gui_design.textbox_design1(649, 262)
surnametxt = my_gui_design.textbox_design1(858, 262)
suffixtxt = my_gui_design.textbox_design1(1067, 262)
date_of_birthtxt = my_gui_design.textbox_design1(440, 330)
nationalitytxt = my_gui_design.textbox_design1(1067, 330)
#display for second frame
departmenttxt = my_gui_design.textbox_design2(232, 500)
designationtxt = my_gui_design.textbox_design2(495, 500)
employee_statustxt = my_gui_design.textbox_design2(760, 500)
employee_numbertxt = my_gui_design.textbox_design2(1025, 500)
contact_numbertxt = my_gui_design.textbox_design2(232, 435)
email_addresstxt = my_gui_design.textbox_design2(495, 435)
other_social_mediatxt = my_gui_design.textbox_design2(760, 435)
social_media_accounttxt = my_gui_design.textbox_design2(1025, 435)
#display for third frame
address_line1txt = my_gui_design.textbox_design2(232, 600)
address_line2txt = my_gui_design.textbox_design2(495, 600)
baranggaytxt = my_gui_design.textbox_design2(760, 600)
municipalittxt = my_gui_design.textbox_design2(1025, 600)
provincetxt = my_gui_design.textbox_design2(232, 670)
zip_codetxt = my_gui_design.textbox_design2(760, 670)
countrytxt = my_gui_design.textbox_design2(495, 670)
picturepathtxt = my_gui_design.textbox_design2(1025, 670)
#textbox label for first frame
firstname_lbl = my_gui_design.label_design(440, 235, 'Firstname')
middle_namelbl = my_gui_design.label_design(650, 235, 'Middlename')
surnamelbl = my_gui_design.label_design(858, 235, 'Surname')
suffixlbl = my_gui_design.label_design(1067, 235, 'Suffix')
date_of_birthlbl = my_gui_design.label_design(440, 305, 'Date of Birth')
nationalitylbl = my_gui_design.label_design(1067, 305, 'Nationality')
civil_statuslbl = my_gui_design.label_design(858, 305, 'Civil Status')
genderlbl = my_gui_design.label_design(650, 305, 'Gender')
#text labal for second frame
departmentlbl = my_gui_design.label_design(232, 410, 'Department')
designationlbl = my_gui_design.label_design(498, 410, 'Designation')
emp_statuslbl = my_gui_design.label_design(764, 410, 'Employee Status')
emp_numberlbl = my_gui_design.label_design(1030, 410, 'Employee Number')
emp_contact_numlbl = my_gui_design.label_design(232, 475, 'Contact Number')
emp_email_addlbl = my_gui_design.label_design(498, 475, 'Email Address')
emp_other_social_media_accountlbl = my_gui_design.label_design(764, 475, 'Other Social Media Account')
emp_social_media_accountlb = my_gui_design.label_design(1030, 475, 'Social Media Account')
#text label for third frame
address_line1txt = my_gui_design.label_design(232, 575, 'Address Line 1')
address_line2txt = my_gui_design.label_design(495, 575, 'Address Line 2 (Optional)')
baranggaytxt = my_gui_design.label_design(760, 575, 'Baranggay')
municipalittxt = my_gui_design.label_design(1025, 575, 'Municipality')
provincetxt = my_gui_design.label_design(232, 645, 'Province')
zip_codetxt = my_gui_design.label_design(498, 645, 'Zip Code')
countrytxt = my_gui_design.label_design(764, 645, 'Country')
picturepathtxt = my_gui_design.label_design(1024, 645, 'Picture Path of Uploaded Image')
#call image to display
uploaded_image = my_gui_design.image_design(r'C:\Users\longa\PycharmProjects\PLDL01E\images.png', 222, 110, 200, 180)
#call for the button and place under the image
uploadbutton = my_gui_design.button_design(263, 300, 'Choose File', 15, '#57a1f8')
savebtn = my_gui_design.button_design(250, 730, 'SAVE', 20, 'blue')
cancelbtn = my_gui_design.button_design(400, 730, 'CANCEL', 20, 'Red')
window.mainloop()
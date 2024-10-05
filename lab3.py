#start

company_name = ""
department = ""
Employee_name = ""
employee_number = ""
cut_off = ""
pay_period = cut_off
rate_per_hr = 0
no_hrs_payday = 0
no_hrs_overtime = 0
no_hrs_absent = 0
no_hrs_tardy = 0
no_hrs_honorarium = 0
basic_pay = 0
overtime_pay = 0
absences = 0
tardiness = 0
honorarium = 0
tax = 0
sss = 0
philhealth = 0
pagibig = 100.00
gross_income = 0
deduction = 0
net_income = 0

company_name = str(input("Enter your Company Name:"))
department = str(input("Enter your department:"))
Employee_name = str(input("Enter your name:"))
employee_number = str(input("Enter your Employee Number:"))
cut_off = str(input("Input your salary date cut off:"))
rate_per_hr = float(input("Input your rate per hour:"))
no_hrs_payday = float(input("Input your number of hours per payday:"))
no_hrs_overtime = float(input("Input the number of overtime hours you take:"))
no_hrs_absent = float(input("Input the number of hours you have been absent:"))
no_hrs_honorarium = float(input("Input the number of hours you have on your honorarium:"))

#calculations

basic_pay = rate_per_hr * no_hrs_payday

overtime_pay = no_hrs_overtime * rate_per_hr

absences = no_hrs_absent * rate_per_hr

honorarium = no_hrs_honorarium * rate_per_hr

tardiness = no_hrs_tardy * rate_per_hr

#if statements

if 4250 < gross_income:
    sss = 180.00
elif 4250 <= gross_income <= 4749.99:
    sss = 202.50
elif 4750 <= gross_income <= 5249.99:
    sss = 225.00
elif 5250 <= gross_income <= 5749.99:
    sss = 247.50
elif 5750 <= gross_income <= 6249.99:
    sss = 270.00
elif 6250 <= gross_income <= 6749.99:
    sss = 299.50
elif 6750 <= gross_income <= 7249.99:
    sss = 315.00
elif 7250 <= gross_income <= 7749.99:
    sss = 337.50
elif 7750 <= gross_income <= 8249.99:
    sss = 360.00
elif 8250 <= gross_income <= 8749.99:
    sss = 382.50
elif 8750 <= gross_income <= 9249.99:
    sss = 405.00
elif 9250 <= gross_income <= 9749.99:
    sss = 427.50
elif 9750 <= gross_income <= 10249.99:
    sss = 450.00
elif 10250 <= gross_income <= 10749.99:
    sss = 472.50
elif 10750 <= gross_income <= 11249.99:
    sss = 495.00
elif 11250 <= gross_income <= 11749.99:
    sss = 517.50
elif 11750 <= gross_income <= 12249.99:
    sss = 540.00
elif 12250 <= gross_income <= 12749.99:
    sss = 562.50
elif 12750 <= gross_income <= 13249.99:
    sss = 585.00
elif 13250 <= gross_income <= 13749.99:
    sss = 607.50
elif 13750 <= gross_income <= 14249.99:
    sss = 630.00
elif 14250 <= gross_income <= 14749.99:
    sss = 652.50
elif 14750 <= gross_income <= 15249.99:
    sss = 675.00
elif 15250 <= gross_income <= 15749.99:
    sss = 697.50
elif 15750 <= gross_income <= 16249.99:
    sss = 720.00
elif 16250 <= gross_income <= 16749.99:
    sss = 742.50
elif 16750 <= gross_income <= 17249.99:
    sss = 765.00
elif 17250 <= gross_income <= 17749.99:
    sss = 832.50
elif 17750 <= gross_income <= 18249.99:
    sss = 855.00
elif 18250 <= gross_income <= 18749.99:
    sss = 877.50
else:
    sss = 900.00

if gross_income == 10000:
    philhealth = 500
elif 10000.01 <= gross_income <= 99999.99:
    philhealth = gross_income * 0.05
elif gross_income == 100000:
    philhealth = 5000
else:
    philhealth = 0

if 0 <= gross_income <= 20832.99:
    tax = 0.00
elif 20833 <= gross_income <= 33332:
    tax = 0.15 * (gross_income - 20833)
elif 33333 <= gross_income <= 66666:
    tax = 1875 + 0.20 * (gross_income - 33333)
elif 66667 <= gross_income <= 166666:
    tax = 8541.80 + 0.25 * (gross_income - 66667)
elif 166666 <= gross_income <= 666666:
    tax = 33541.80 + 0.30 * (gross_income - 166667)
else:
    tax = 183541.80 + 0.35 * (gross_income - 666667)


deduction = absences + tardiness + tax + sss + philhealth + sss + pagibig

net_income = gross_income - deduction

print("Company name: ", company_name)
print("Department: ", department)
print("Employee Code: ", employee_number)
print("Employee Name: ", Employee_name)
print("Cut-off", cut_off)
print("Pay period:", pay_period)
print("Basic Pay:", basic_pay)
print("Overtime: ", overtime_pay)
print("Absences: ", absences)
print("Honorarium:", honorarium)
print("Tardy:", tardiness)
print("Withholding Tax:", tax)
print("SSS Contribution:", sss)
print("Pagibig Contribution", pagibig)
print("Philhealth Contribution", philhealth)
print("Deductions: ", deduction)
print("Gross Income:", gross_income)
print("Net Income: ", net_income)

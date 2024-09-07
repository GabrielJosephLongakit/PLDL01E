#initialization
name_employee = " "
dept_employee = " "
rate_per_hr = 0
num_hrs_day = 0
num_days_wk = 0
num_wks_mth = 0
total_deduction = 0
gross_income = 0
SSS_contri = 0
philhealth_contri = 0
pagibig_contri = 100.00
net_income = 0

#input
name_employee = str(input("Please enter your Employee Name: "))
dept_employee = str(input("Please enter your Department: "))
rate_per_hr = float(input("Please enter your rate per hour: "))
num_hrs_day = float(input("Please enter your number of hours per day: "))
num_days_wk = float(input("Please enter your number of days per week:"))
num_wks_mth = float(input("Please enter your number of weeks per month: "))

#formulas
gross_income = rate_per_hr * num_hrs_day * num_days_wk * num_wks_mth

#if then

if 0 <= gross_income <= 20000:
    philhealth_contri = 125.75
    SSS_contri = 100.00
elif 20001 <= gross_income <= 50000:
    philhealth_contri = 2200.50
    SSS_contri = 1200.00
elif 50001 <= gross_income <= 75000:
    philhealth_contri = 4800.00
    SSS_contri = 6800.00
elif 75001 < gross_income:
    philhealth_contri = 5800.00
    SSS_contri = 8800.00

#total deduction

total_deduction = SSS_contri + pagibig_contri + philhealth_contri

#net income
net_income = gross_income - total_deduction

#print net income
print("Employee Name and Department:", name_employee, dept_employee)
print("Total Deduction of Employee:", total_deduction)
print("Gross Income:", gross_income)
print("Net Income:", net_income)
import midtermexam

#get inputs from maynilad bill class

obj1 = midtermexam.maynilad_bill
acct_no = int(input("Contract Account No.:"))
name = input("Account Name:")
address = input("Address:")
TIN = input("TIN:")
rate_class = input("Rate Class: ")
business_area = input("Business Area:: ")

#get inputs from metering info
obj2 = midtermexam.metering_info
meter_no = input("Meter No.: ")
MRU_no = float(input("MRU No.: "))
seq_no = int(input("Seq No.: "))
reading_date = input("Reading Date: ")
present_reading = int(input("Present Reading: "))
previous_reading = int(input("Previous Reading:"))
consumption = int(input("Consumption: "))

#get inputs from billing summary

obj3 = midtermexam.billing_summary
billing_period = input("Billing Period: ")
current_charges = float(input("Current Charges: "))
basic_charge = float(input("Basic Charges: "))
environmental_charges = float(input("Environmental Charges (20% of Basic Charge):"))
maintenance_charge = float(input("Maintenance Service Charge (MSC): "))
charges_before_taxes = float(input("Total Current Charges Before Taxes: "))
government_taxes = float(input("Government Taxes: "))
payment_due_date = input("Payment Due Date: ")

#computation for basic charge
basic_charge = 23.52 * consumption

#computation for total amount due

total_amount_due = charges_before_taxes + government_taxes

#computation for total charges before taxes

charges_before_taxes = basic_charge + environmental_charges + maintenance_charge

#computation for environmental charges
environmental_charges = basic_charge * 0.20

#computation for government taxes

government_taxes = charges_before_taxes * 0.025

#creation of the maynilad receipt

print("---------------------------------------------------------------------------------------------")
print("                                                             Maynilad Water Services, Inc. \t")
print("                                                             8390 DR A SANTOS AVE BF HOMES \t")
print("                         Maynilad                            PARANAQUE CITY")
print("                                                             SPM No.:")
print("                                                             Machine SN:")
print("SOA  #   00000000003456789012")
print("                                \t STATEMENT OF ACCOUNT \t                                     ")
print("                            \t For the Month of: February 2024 \t                              ")
print("                                                                                               ")
print("                                 \t SERVICE INFORMATION \t                                     ")
print("                                                                                               ")
print("Contract Account No. :", acct_no)
print("Account Name         :", name)
print("Service Address      :", address)
print("TIN                  :", TIN)
print("Rate Class           :", rate_class)
print("Business Area        :", business_area)
print("----------------------------------------------------------------------------------------------")
print("                                \t METERING INFORMATION \t                                    ")
print("Meter No.:", meter_no,           "MRU No.:", MRU_no,                          "Seq No.", seq_no)
print("Reading Date      :", reading_date)
print("Present Reading   :", present_reading)
print("Previous Reading  :", previous_reading)
print("Consumption (cu.m):", consumption)
print("                                                                                              ")
print("Previous 3 Months                                                                             ")
print("  Consumption                                                                                 ")
print("----------------------------------------------------------------------------------------------")
print("                                \t BILL & PAYMENT HISTORY \t                                  ")
print("                                                                                              ")
print("Desc          Total Amount                            OR#                                 Date")
print("                                                                                              ")
print("----------------------------------------------------------------------------------------------")
print("                                   \t BILLING SUMMARY \t                                      ")
print("BILLING PERIOD                                                               :", billing_period)
print("Current Charges                                                              :", current_charges)
print("Basic Charge                                                                 :", basic_charge)
print("Environmental Charges (20% of Basic Charge)                                  :", environmental_charges)
print("Maintenance Service Charge (MSC)                                             :", maintenance_charge)
print("Total Current Charges Before Taxes                                           :", charges_before_taxes)
print("Government Taxes                                                             :", government_taxes)
print("                                                                                              ")
print("----------------------------------------------------------------------------------------------")
print("TOTAL AMOUNT DUE                                                             :", total_amount_due)
print("PAYMENT DUE DATE                                                             :", payment_due_date)
print("----------------------------------------------------------------------------------------------")
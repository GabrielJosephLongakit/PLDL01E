import midtermquiz


def __init__(self):
    self.name = ""
    self.address = ""
    self.rate = ""
    self.service_id = ""
    self.account_number = ""
    self.previous_billing = 0
    self.meter_reading_date = ""
    self.amount_due = 0
    self.due_date = ""
    self.bill_period = ""
    self.total_kwh = 0
    self.total_current_amount = 0
    self.rate_per_kilowatts = ""


class billing_statement:

    def __init__(self):
        self.name = input("Name:")
        self.address = input("Address:")
        self.rate = input("Rate: ")
        self.service_id = input("Service ID Number: ")
        self.account_number = input("Customer Account Number (CAN): ")
        self.previous_billing = float(input("Balance from Previous Billing:"))
        self.meter_reading_date = input("Enter Meter Reading Date")
        self.amount_due = float(input("Amount due: "))
        self.due_date = input("Due date: ")
        self.bill_period = input("Bill Period: ")
        self.total_kwh = int(input("Total KWH: "))
        self.total_current_amount = float(input("Total Current Amount: "))
        self.rate_per_kilowatts = input("Rate per kilowatt: ")





        def __display_receipt__(self):
        print("Name:", self.name)
        print("Address:", self.address)
        print("")
        print("=================================================")
        print("Service Info")
        print("Service ID Number:", self.service_id)
        print("Rate (Residential or Commercial):", self.rate)
        print("=================================================")
        print("Billing Info")
        print("Bill Period:", self.bill_period)
        print("Due Date:", self.due_date)
        print("Total KWH:", self.total_kwh)
        print("Total Current Amount", self.total_current_amount)
        print("=================================================")
        print("Rate this month", self.rate_per_kilowatts)
        print("Actual Consumption:", self.actual_consumption)
        print("Charges", self.charges)


class ElectricityBill:
    def __init__(self, previous_balance, generation, transmission, system_loss, distribution, subsidies, taxes, universal, fit_all, installment=0):
        self.previous_balance = previous_balance
        self.generation = generation
        self.transmission = transmission
        self.system_loss = system_loss
        self.distribution = distribution
        self.subsidies = subsidies
        self.govt_taxes = taxes
        self.universal = universal
        self.fit_all = fit_all
        self.installment = installment
 def __display_receipt__(self):
        print("Name:", self.name)
        print("Address:", self.address)
        print("")
        print("=================================================")
        print("Service Info")
        print("Service ID Number:", self.service_id)
        print("Rate (Residential or Commercial):", self.rate)
        print("=================================================")
        print("Billing Info")
        print("Bill Period:", self.bill_period)
        print("Due Date:", self.due_date)
        print("Total KWH:", self.total_kwh)
        print("Total Current Amount", self.total_current_amount)
        print("=================================================")
        print("Rate this month", self.rate_per_kilowatts)
        print("Actual Consumption:", self.actual_consumption)
        print("Charges", self.charges)

emp1 = ElectricityBill()
emp1.__display_receipt__
class electric_bill:

#input all data for Electical Bill


    def __bill_computation__(self):
        self.actual_consumption = int(input("Actual Consumption: "))
        self.generation = float(input("Generation:"))
        self.transmission = float(input("Transmission:"))
        self.system_loss = float(input("System Loss:"))
        self.distribution = float(input("Distribution (Meralco): "))
        self.subsidies = float(input("Subsidies:"))
        self.govt_taxes = float(input("Government Taxes: "))
        self.universal_charges = float(input("Universal Charges:"))
        self.Fit_all = float(input("Fit-All (Renewable): "))
        self.other_charges = float(input("Other Charges: "))

#Finding out if the user has paid the previous balance or not.
    def __previous_billing__(self):
        if self.previous_billing > 0:
            self.please_pay = print("Please pay your remaining balance: ")
        else:
            self.thank_you = print("Thank you")

#Computation of kilowatts and consumption in order to find the raw amount due.
    def __charges_for_billing__(self):
        self.charges = self.rate_per_kilowatts * self.actual_consumption

#Computing of Total Amount Due
    def __total_computation__(self):
        self.amount_due = self.previous_billing + self.charges

#displaying of data and total bill

electric_bill()
emp1__bill_computation__()
emp1.__previous_billing__()
emp1.__charges_for_billing__()
emp1.__total_computation__()
emp1.__display_receipt__()

class maynilad_bill:
#input for service information
    def __init__(self):
        self.acct_no = ""
        self.name = ""
        self.address = ""
        self.TIN = ""
        self.rate_class = ""
        self.business_area = ""

#call and assign the variables
    def service_info(self, acct_no, name, address, TIN, rate_class, business_area):
        self.acct_no = acct_no
        self.name = name
        self.address = address
        self.TIN = TIN
        self.rate_class = rate_class
        self.business_area = business_area
#display your inputs
    def display_service_info(self):
        print("Account Number: ", self.acct_no)
        print("Name: ", self.name)
        print("Address:", self.address)
        print("TIN", self.TIN)
        print("Rate Class:", self.rate_class)
        print("Business Area:", self.business_area)

class metering_info:
    #input for metering information
    def __init__(self):
        self.meter_no = ""
        self.MRU_no = 0
        self.seq_no = 0
        self.reading_date = ""
        self.present_reading = 0
        self.previous_reading = 0
        self.consumption = 0


    #call all variables

    def meter_info(self, meter_no, MRU_no, seq_no, reading_date, present_reading, previous_reading, consumption):
        self.meter_no = meter_no
        self.MRU_no = MRU_no
        self.seq_no = seq_no
        self.reading_date = reading_date
        self.present_reading = present_reading
        self.previous_reading = previous_reading
        self.consumption = consumption


#print your inputs

    def display_meter_info(self):
        print("Meter Number:", self.meter_no)
        print("MRU Number:", self.MRU_no)
        print("Sequence Number:", self.seq_no)
        print("Reading Date:", self.reading_date)
        print("Present Reading", self.present_reading)
        print("Previous Reading", self.previous_reading)
        print("Consumption (cu.m):", self.consumption)
#input for billing summary
class billing_summary:
    def __init__(self):
        self.billing_period = ""
        self.current_charges = 0
        self.basic_charge = 0
        self.environmental_charges = 0
        self.maintenance_charge = 1.5
        self.charges_before_taxes = 0
        self.government_taxes = 0
        self.total_amount_due = 0
        self.payment_due_date = ""

#assign your variables
    def billing_summary(self, billing_period, current_charges, basic_charge, environmental_charges, maintenance_charge, charges_before_taxes, government_taxes, total_amount_due, payment_due_date):
        self.billing_period = billing_period
        self.current_charges = current_charges
        self.basic_charge = basic_charge
        self.environmental_charges = environmental_charges
        self.maintenance_charge = maintenance_charge
        self.charges_before_taxes = charges_before_taxes
        self.government_taxes = government_taxes
        self.total_amount_due = total_amount_due
        self.payment_due_date = payment_due_date
#computation for billing
    def computation_for_total_charges(self):
        self.charges_before_taxes = self.basic_charge + self.environmental_charges + self.maintenance_charge
#compute for environmental charge
    def environmental_charges_correction(self):
        self.environmental_charges = self.basic_charge * 0.20
#compute for government taxes
    def computation_for_government_taxes(self):
        self.government_taxes = self.charges_before_taxes * 0.025
#compute for total ampount due
    def computation_for_total_amount_due(self):
        self.total_amount_due = self.charges_before_taxes + self.government_taxes


#display your data
    def display_billing_summary(self):
        print("Billing Period:", self.billing_period)
        print("Current Charges:", self.current_charges)
        print("Basic Charge:", self.basic_charge)
        print("Environmental Changes:", self.environmental_charges)
        print("Maintenance Service Charge (MSC): ", self.maintenance_charge)
        print("Total Current Charges Before Taxes:", self.charges_before_taxes)
        print("Government Taxes: ", self.government_taxes)
        print("TOTAL AMOUNT DUE:", self.total_amount_due)
        print("PAYMENT DUE DATE:", self.payment_due_date)

class Student:
    oneunit = 1551.00
    def __init__(self):
        self.one_unit = 1551.00
        self.student_name = input("Enter Student Name:")
        self.course = input("Enter your course:")
        self.student_number = input("Enter your student number:")
        self.academic_year = input("Enter your current Academic Year:")

        self.current_date = input("Enter the date today:")

        self.section = []
        self.subject = []
        self.units = []

        for i in range(5):
            self.section.append = (input(f"Enter your section {i + 1}: "))
            self.subject.append = (input(f"Enter the subject {i + 1}: "))
            self.units.append = (float(input(f"Enter the units {i + 1}:")))


        self.adu_chronicle = float(input("Enter the AdU Chronicle Fee:"))
        self.athletic = float(input("Enter your athletic fee:"))
        self.avl = float(input("Enter you Audio-Visual Library Fee:"))
        self.ausg = float(input("Enter your AUSG Fee:"))
        self.cultural = float(input("Enter your Cultural Fee:"))
        self.energy_fee = float(input("Enter the Energy Fee:"))
        self.guidance = float(input("Enter your Guidance Fee:"))
        self.insurance = float(input("Enter your Insurance Fee:"))
        self.lms = float(input("Enter your LMS Fee:"))
        self.library = float(input("Enter you Library Fee:"))
        self.medical = float(input("Enter your Medical Fee:"))
        self.registration = float(input("Enter your registration fee:"))
        self.rso = float(input("Enter your RSO Fee:"))
        self.student_act = float(input("Enter your Student Activities Fee:"))
        self.student_nurture = float(input("Enter your Student Nurturance Fee:"))
        self.tech_fee = float(input("Enter your Technology Fee:"))
        self.papers = float(input("Enter the Test Paper Fee:"))
        self.downpayment = float(input("Enter your Downpayment amount:"))


    def computation_tuition_fee_lecture(self):
        total_units = sum(self.units)
        self.tuition_fee_lecture = 1551.00 * total_units

    def computation_assessment_amt(self):
        self.assessment_amt = self.adu_chronicle + self.athletic + self.avl + self.ausg + self.cultural + self.energy_fee + self.guidance + self.insurance + self.lms + self.library + self.medical + self.registration + self.rso + self.student_act + self.student_nurture + self.tech_fee + self.papers

    def computation_total_due(self):
        self.total_due = self.assessment_amt - self.downpayment

    def balance_inquiry(self):
        self.balance = self.total_due/3
    def display_Student(self):
        print("Student Name: ", self.student_name)
        print("Program: ", self.course)
        print("Student Number: ", self.student_number)
        print("Academic Year: ", self.academic_year)
        for i in range(5):
            print("Section", self.section, "Subjects", self.subject, "Units:", self.units)
        print("=========================================================================")
        print("=========================================================================")
        print("Tuition Fee: ", self.tuition_fee_lecture)
        print("AdU Chronicle: ", self.adu_chronicle)
        print("Athletic: ", self.athletic)
        print("Audio-Visual Library: ", self.avl)
        print("AUSG: ", self.ausg)
        print("Cultural Fee: ", self.cultural)
        print("Energy Cost: ", self.energy_fee)
        print("Guidance: ", self.guidance)
        print("Insurance Fee: ", self.insurance)
        print("Learning Management System: ", self.lms)
        print("Library Fee: ", self.library)
        print("Medical and Dental: ", self.medical)
        print("Registration: ", self.registration)
        print("RSO: ", self.rso)
        print("Student Activities Fee: ", self.student_act)
        print("Student Nurturance Fee: ", self.student_nurture)
        print("Technology Fee: ", self.tech_fee)
        print("Test Papers: ", self.papers)
        print("---------------------------------------------")
        print("Assessment Amount: ", self.assessment_amt)
        print("Downpayment: ", self.downpayment)
        print("---------------------------------------------")
        print("Total Due:", self.total_due)
        print("")
        print("Prelims: ", self.balance)
        print("Midterms:", self.balance)
        print("Finals: ", self.balance)



student = Student()
student.computation_tuition_fee_lecture()
student.computation_assessment_amt()
student.computation_total_due()
student.balance_inquiry()



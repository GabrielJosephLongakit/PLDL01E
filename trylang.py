import tkinter as tk
from tkinter import ttk

class ApplicationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Accredited Meralco Contractors (AMC) Application Form")
        self.create_widgets()

    def create_widgets(self):
        # Header
        header_frame = tk.Frame(self.root)
        header_frame.pack(pady=10)

        logo_label = tk.Label(header_frame, text="Meralco", font=("Arial", 18, "bold"), fg="orange")
        logo_label.pack(side=tk.LEFT, padx=5)

        title_label = tk.Label(header_frame, text="ACCREDITED MERALCO CONTRACTORS (AMC)\nAPPLICATION FORM",
                               font=("Arial", 14, "bold"), justify=tk.CENTER)
        title_label.pack(side=tk.LEFT, padx=5)

        type_accommodation_frame = tk.Frame(self.root)
        type_accommodation_frame.pack(pady=10)

        type_label = tk.Label(type_accommodation_frame, text="Type of accommodation:", font=("Arial", 10))
        type_label.grid(row=0, column=0, sticky="w")

        self.hmb_var = tk.BooleanVar()
        self.sme_var = tk.BooleanVar()

        hmb_check = tk.Checkbutton(type_accommodation_frame, text="Home and Microbiz (HMB)", variable=self.hmb_var)
        hmb_check.grid(row=1, column=0, sticky="w")

        sme_check = tk.Checkbutton(type_accommodation_frame, text="Small and Medium Enterprise (SME)", variable=self.sme_var)
        sme_check.grid(row=2, column=0, sticky="w")

        # Application Information
        app_info_frame = tk.LabelFrame(self.root, text="APPLICATION INFORMATION", font=("Arial", 10, "bold"))
        app_info_frame.pack(fill="both", expand="yes", padx=10, pady=5)

        tk.Label(app_info_frame, text="Business Name:").grid(row=0, column=0, sticky="w")
        self.business_name_entry = tk.Entry(app_info_frame)
        self.business_name_entry.grid(row=0, column=1, sticky="w", padx=5)

        tk.Label(app_info_frame, text="Office Address:").grid(row=1, column=0, sticky="w")
        self.office_address_entry = tk.Entry(app_info_frame)
        self.office_address_entry.grid(row=1, column=1, sticky="w", padx=5)

        tk.Label(app_info_frame, text="Landline No:").grid(row=2, column=0, sticky="w")
        self.landline_entry = tk.Entry(app_info_frame)
        self.landline_entry.grid(row=2, column=1, sticky="w", padx=5)

        tk.Label(app_info_frame, text="Fax No:").grid(row=3, column=0, sticky="w")
        self.fax_entry = tk.Entry(app_info_frame)
        self.fax_entry.grid(row=3, column=1, sticky="w", padx=5)

        tk.Label(app_info_frame, text="E-mail Address:").grid(row=4, column=0, sticky="w")
        self.email_entry = tk.Entry(app_info_frame)
        self.email_entry.grid(row=4, column=1, sticky="w", padx=5)

        # Representative Information
        rep_info_frame = tk.LabelFrame(self.root, text="REPRESENTATIVE INFORMATION", font=("Arial", 10, "bold"))
        rep_info_frame.pack(fill="both", expand="yes", padx=10, pady=5)

        tk.Label(rep_info_frame, text="Name-Position:").grid(row=0, column=0, sticky="w")
        self.name_position_entry = tk.Entry(rep_info_frame)
        self.name_position_entry.grid(row=0, column=1, sticky="w", padx=5)

        tk.Label(rep_info_frame, text="Landline or Mobile No:").grid(row=1, column=0, sticky="w")
        self.rep_landline_entry = tk.Entry(rep_info_frame)
        self.rep_landline_entry.grid(row=1, column=1, sticky="w", padx=5)

        tk.Label(rep_info_frame, text="Fax No:").grid(row=2, column=0, sticky="w")
        self.rep_fax_entry = tk.Entry(rep_info_frame)
        self.rep_fax_entry.grid(row=2, column=1, sticky="w", padx=5)

        tk.Label(rep_info_frame, text="E-mail Address:").grid(row=3, column=0, sticky="w")
        self.rep_email_entry = tk.Entry(rep_info_frame)
        self.rep_email_entry.grid(row=3, column=1, sticky="w", padx=5)

        # Affiliation and Type
        affiliation_frame = tk.Frame(self.root)
        affiliation_frame.pack(pady=10)

        self.type_var = tk.StringVar()
        tk.Label(affiliation_frame, text="Official Representatives:").grid(row=0, column=0, sticky="w")
        tk.Radiobutton(affiliation_frame, text="Single Proprietorship", variable=self.type_var, value="Single Proprietorship").grid(row=1, column=0, sticky="w")
        tk.Radiobutton(affiliation_frame, text="Partnership", variable=self.type_var, value="Partnership").grid(row=2, column=0, sticky="w")
        tk.Radiobutton(affiliation_frame, text="Corporation", variable=self.type_var, value="Corporation").grid(row=3, column=0, sticky="w")
        tk.Radiobutton(affiliation_frame, text="Cooperative", variable=self.type_var, value="Cooperative").grid(row=4, column=0, sticky="w")

        self.affiliation_var = tk.StringVar()
        tk.Label(affiliation_frame, text="Affiliation:").grid(row=5, column=0, sticky="w")
        tk.Checkbutton(affiliation_frame, text="Institute of Integrated Electrical Engineers (IIEE)", variable=self.affiliation_var).grid(row=6, column=0, sticky="w")
        tk.Checkbutton(affiliation_frame, text="Society in Philippine Electrotechnical Constructors and Suppliers Inc. (SPECS)", variable=self.affiliation_var).grid(row=7, column=0, sticky="w")

if __name__ == "__main__":
    root = tk.Tk()
    app = ApplicationForm(root)
    root.mainloop()

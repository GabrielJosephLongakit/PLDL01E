import tkinter as tk
from tkinter import ttk, messagebox


def calculate_total():
    try:
        tuition_fee = float(entry_tuition.get())
        misc_fee = float(entry_misc.get())
        lab_fee = float(entry_lab.get())
        other_fees = float(entry_other.get())
        installment_charge = float(entry_installment.get())
        payments_made = float(entry_payments.get())

        total = tuition_fee + misc_fee + lab_fee + other_fees + installment_charge
        balance = total - payments_made

        label_total['text'] = f"Total Assessment: {total:.2f}"
        label_balance['text'] = f"Balance: {balance:.2f}"
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for all fields.")


def submit_form():
    student_name = entry_name.get()
    student_number = entry_number.get()

    if not student_name or not student_number:
        messagebox.showerror("Input Error", "Please fill in all required fields.")
    else:
        messagebox.showinfo("Submission Success", "Form submitted successfully!")


# Main application window
root = tk.Tk()
root.title("Enrollment Assessment Form")
root.geometry("600x700")

# Title
header = tk.Label(root, text="Enrollment Assessment Form", font=("Arial", 16, "bold"))
header.pack(pady=10)

# Student Information
frame_info = tk.LabelFrame(root, text="Student Information", padx=10, pady=10)
frame_info.pack(fill="x", padx=10, pady=5)

label_name = tk.Label(frame_info, text="Name:")
label_name.grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame_info, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_number = tk.Label(frame_info, text="Student Number:")
label_number.grid(row=1, column=0, sticky="w")
entry_number = tk.Entry(frame_info, width=30)
entry_number.grid(row=1, column=1, padx=10, pady=5)

# Fee Details
frame_fees = tk.LabelFrame(root, text="Fees", padx=10, pady=10)
frame_fees.pack(fill="x", padx=10, pady=5)

label_tuition = tk.Label(frame_fees, text="Tuition Fee:")
label_tuition.grid(row=0, column=0, sticky="w")
entry_tuition = tk.Entry(frame_fees, width=15)
entry_tuition.grid(row=0, column=1, padx=10, pady=5)

label_misc = tk.Label(frame_fees, text="Miscellaneous Fees:")
label_misc.grid(row=1, column=0, sticky="w")
entry_misc = tk.Entry(frame_fees, width=15)
entry_misc.grid(row=1, column=1, padx=10, pady=5)

label_lab = tk.Label(frame_fees, text="Laboratory Fees:")
label_lab.grid(row=2, column=0, sticky="w")
entry_lab = tk.Entry(frame_fees, width=15)
entry_lab.grid(row=2, column=1, padx=10, pady=5)

label_other = tk.Label(frame_fees, text="Other Fees:")
label_other.grid(row=3, column=0, sticky="w")
entry_other = tk.Entry(frame_fees, width=15)
entry_other.grid(row=3, column=1, padx=10, pady=5)

label_installment = tk.Label(frame_fees, text="Installment Charge:")
label_installment.grid(row=4, column=0, sticky="w")
entry_installment = tk.Entry(frame_fees, width=15)
entry_installment.grid(row=4, column=1, padx=10, pady=5)

label_payments = tk.Label(frame_fees, text="Payments Made:")
label_payments.grid(row=5, column=0, sticky="w")
entry_payments = tk.Entry(frame_fees, width=15)
entry_payments.grid(row=5, column=1, padx=10, pady=5)

# Output Labels
frame_output = tk.Frame(root)
frame_output.pack(fill="x", padx=10, pady=10)

label_total = tk.Label(frame_output, text="Total Assessment: ", font=("Arial", 12))
label_total.pack(anchor="w")
label_balance = tk.Label(frame_output, text="Balance: ", font=("Arial", 12))
label_balance.pack(anchor="w")

# Buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_calculate = tk.Button(frame_buttons, text="Calculate", command=calculate_total, bg="blue", fg="white", width=10)
btn_calculate.grid(row=0, column=0, padx=10)

btn_submit = tk.Button(frame_buttons, text="Submit", command=submit_form, bg="green", fg="white", width=10)
btn_submit.grid(row=0, column=1, padx=10)

btn_exit = tk.Button(frame_buttons, text="Exit", command=root.quit, bg="red", fg="white", width=10)
btn_exit.grid(row=0, column=2, padx=10)

# Run the application
root.mainloop()

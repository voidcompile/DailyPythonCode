import tkinter as tk
from tkinter import messagebox
from datetime import datetime, date

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        birth_date = date(year, month, day)
        today = date.today()

        if birth_date > today:
            messagebox.showerror("Error", "Birth date cannot be in the future!")
            return

        delta = today - birth_date
        years = delta.days // 365
        months = (delta.days % 365) // 30
        days = (delta.days % 365) % 30

        result_label.config(text=f"You are {years} years, {months} months, and {days} days old.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for day, month, and year.")

# GUI setup
root = tk.Tk()
root.title("Age Calculator")
root.geometry("350x300")
root.resizable(False, False)

tk.Label(root, text="Enter your birth date", font=("Helvetica", 14)).pack(pady=10)

form_frame = tk.Frame(root)
form_frame.pack()

tk.Label(form_frame, text="Day").grid(row=0, column=0, padx=5, pady=5)
day_entry = tk.Entry(form_frame, width=5)
day_entry.grid(row=1, column=0, padx=5)

tk.Label(form_frame, text="Month").grid(row=0, column=1, padx=5, pady=5)
month_entry = tk.Entry(form_frame, width=5)
month_entry.grid(row=1, column=1, padx=5)

tk.Label(form_frame, text="Year").grid(row=0, column=2, padx=5, pady=5)
year_entry = tk.Entry(form_frame, width=8)
year_entry.grid(row=1, column=2, padx=5)

tk.Button(root, text="Calculate Age", command=calculate_age, bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=20)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack()

root.mainloop()

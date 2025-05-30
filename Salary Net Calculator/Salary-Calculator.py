import tkinter as tk
from tkinter import messagebox

class SalaryCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Salary Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.expense_entries = []

        # Salary input
        tk.Label(root, text="Enter your salary:", font=("Arial", 12)).pack(pady=10)
        self.salary_entry = tk.Entry(root, font=("Arial", 12))
        self.salary_entry.pack(pady=5)

        # Expense section
        tk.Label(root, text="Enter your expenses:", font=("Arial", 12, "bold")).pack(pady=10)

        for i, label in enumerate(["Installments", "Shopping", "Taxes", "Fuel", "Other"]):
            frame = tk.Frame(root)
            frame.pack(pady=3)
            tk.Label(frame, text=f"{label}:", width=15, anchor="w").pack(side=tk.LEFT)
            entry = tk.Entry(frame)
            entry.pack(side=tk.LEFT)
            self.expense_entries.append(entry)

        # Calculate button
        tk.Button(root, text="Calculate Net Salary", command=self.calculate, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=20)

        # Output
        self.result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
        self.result_label.pack(pady=10)

    def calculate(self):
        try:
            salary = float(self.salary_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid salary.")
            return

        total_expenses = 0
        for entry in self.expense_entries:
            val = entry.get()
            if val.strip():
                try:
                    total_expenses += float(val)
                except ValueError:
                    messagebox.showerror("Input Error", "All expenses must be numbers.")
                    return

        net = salary - total_expenses
        self.result_label.config(text=f"Net Remaining: ${net:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SalaryCalculator(root)
    root.mainloop()

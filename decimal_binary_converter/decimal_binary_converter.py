import tkinter as tk
from tkinter import ttk, messagebox

class DecimalBinaryConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Decimal ↔ Binary Converter")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Decimal ↔ Binary Converter", font=("Helvetica", 14, "bold")).pack(pady=10)

        # Conversion direction
        dir_frame = tk.Frame(self.root)
        dir_frame.pack(pady=5)
        tk.Label(dir_frame, text="Convert:", font=("Helvetica", 11)).pack(side=tk.LEFT, padx=(0, 10))

        self.direction = tk.StringVar(value="Dec → Bin")
        combo = ttk.Combobox(dir_frame, textvariable=self.direction, state="readonly", width=10, font=("Helvetica", 11))
        combo['values'] = ("Dec → Bin", "Bin → Dec")
        combo.current(0)
        combo.pack(side=tk.LEFT)

        # Input field
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)
        tk.Label(input_frame, text="Enter value:", font=("Helvetica", 11)).pack(side=tk.LEFT, padx=(0, 10))
        self.input_entry = tk.Entry(input_frame, font=("Helvetica", 11), width=20)
        self.input_entry.pack(side=tk.LEFT)

        # Convert button
        tk.Button(
            self.root,
            text="Convert",
            command=self.convert,
            bg="#007ACC",
            fg="white",
            font=("Helvetica", 11)
        ).pack(pady=10)

        # Result label
        self.result_label = tk.Label(self.root, text="", font=("Courier", 12))
        self.result_label.pack(pady=10)

    def convert(self):
        val = self.input_entry.get().strip()
        direction = self.direction.get()

        if direction == "Dec → Bin":
            # Decimal to binary
            try:
                dec = int(val)
                if dec < 0:
                    raise ValueError
                binary = bin(dec)[2:]
                self.result_label.config(text=f"Binary: {binary}")
            except ValueError:
                messagebox.showerror(
                    "Invalid Input",
                    "Please enter a valid non-negative decimal integer."
                )
                self.result_label.config(text="")
        else:
            # Binary to decimal
            if all(c in '01' for c in val) and val != "":
                try:
                    dec = int(val, 2)
                    self.result_label.config(text=f"Decimal: {dec}")
                except ValueError:
                    messagebox.showerror("Invalid Input", "Conversion error. Please check input.")
                    self.result_label.config(text="")
            else:
                messagebox.showerror(
                    "Invalid Input",
                    "Please enter a valid binary string (only 0s and 1s)."
                )
                self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = DecimalBinaryConverter(root)
    root.mainloop()

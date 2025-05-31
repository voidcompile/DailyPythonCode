import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

class PlotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Plot Generator")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        tk.Label(root, text="Select Plot Type:", font=("Arial", 12)).pack(pady=10)

        self.plot_type = tk.StringVar()
        self.plot_dropdown = ttk.Combobox(root, textvariable=self.plot_type, state="readonly", font=("Arial", 11))
        self.plot_dropdown['values'] = ("Line Plot", "Scatter Plot")
        self.plot_dropdown.current(0)
        self.plot_dropdown.pack(pady=5)

        tk.Label(root, text="Enter X values (comma-separated):", font=("Arial", 11)).pack(pady=10)
        self.x_entry = tk.Entry(root, font=("Arial", 11), width=40)
        self.x_entry.pack()

        tk.Label(root, text="Enter Y values (comma-separated):", font=("Arial", 11)).pack(pady=10)
        self.y_entry = tk.Entry(root, font=("Arial", 11), width=40)
        self.y_entry.pack()

        tk.Button(root, text="Generate Plot", command=self.generate_plot, bg="#2196F3", fg="white", font=("Arial", 12)).pack(pady=20)

    def generate_plot(self):
        try:
            x_vals = list(map(float, self.x_entry.get().split(",")))
            y_vals = list(map(float, self.y_entry.get().split(",")))

            if len(x_vals) != len(y_vals):
                raise ValueError("X and Y must have the same number of values")

            plt.figure(figsize=(6,4))
            if self.plot_type.get() == "Line Plot":
                plt.plot(x_vals, y_vals, marker='o')
            else:
                plt.scatter(x_vals, y_vals)

            plt.title(self.plot_type.get())
            plt.xlabel("X values")
            plt.ylabel("Y values")
            plt.grid(True)
            plt.tight_layout()
            plt.show()

        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PlotApp(root)
    root.mainloop()

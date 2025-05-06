import tkinter as tk

# Colors and style configuration
BG_COLOR = "#F0F4F8"           # Light background
BTN_BG = "#DCEEFF"             # Light blue buttons
BTN_TEXT = "#003366"           # Dark text
BTN_HOVER = "#B3E5FC"          # Hover color
FONT = ("Helvetica", 18)

# Function to handle button clicks
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry_var.set(result)
        except:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry.get() + text)

# Initialize main window
root = tk.Tk()
root.title("Cool Calculator")
root.geometry("320x430")
root.configure(bg=BG_COLOR)

# Entry display field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font=("Helvetica", 24), bd=0, relief="flat", justify="right", bg="white", fg="#333")
entry.pack(pady=20, padx=20, ipady=10, fill=tk.X)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

# Hover effect for buttons
def on_enter(e):
    e.widget["bg"] = BTN_HOVER

def on_leave(e):
    e.widget["bg"] = BTN_BG

# Create buttons
for row_vals in buttons:
    row = tk.Frame(root, bg=BG_COLOR)
    row.pack(expand=True, fill="both", padx=20, pady=5)

    for val in row_vals:
        btn = tk.Button(row, text=val, font=FONT, bg=BTN_BG, fg=BTN_TEXT, bd=0, relief="flat", cursor="hand2")
        btn.pack(side="left", expand=True, fill="both", padx=5, pady=5, ipadx=10, ipady=10)
        btn.bind("<Button-1>", click)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

root.mainloop()

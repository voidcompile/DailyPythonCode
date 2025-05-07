import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# Function to generate a random password
def generate_password():
    length = length_var.get()
    
    if length < 4:
        messagebox.showerror("Error", "Password length must be at least 4 characters!")
        return

    characters = ""
    if use_upper.get():
        characters += string.ascii_uppercase
    if use_lower.get():
        characters += string.ascii_lowercase
    if use_digits.get():
        characters += string.digits
    if use_symbols.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Select at least one character type!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_entry.get()
    pyperclip.copy(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Main window setup
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("420x400")
root.config(bg="#fdfbf7")  # Cream background

# Title Label
title = tk.Label(root, text="🔐 Secure Password Generator", font=("Helvetica", 16, "bold"), bg="#fdfbf7", fg="#2d3e50")
title.pack(pady=10)

# Entry box to display the password
password_entry = tk.Entry(root, font=("Courier New", 14), justify='center', width=32, bd=2, relief="groove")
password_entry.pack(pady=10)

# Copy button
copy_btn = tk.Button(root, text="📋 Copy", command=copy_to_clipboard, bg="#d2f0f3", fg="#1b2a49", width=10)
copy_btn.pack()

# Password length selection
length_frame = tk.Frame(root, bg="#fdfbf7")
length_frame.pack(pady=15)
tk.Label(length_frame, text="Password Length:", font=("Arial", 10), bg="#fdfbf7").pack(side="left")
length_var = tk.IntVar(value=12)
tk.Spinbox(length_frame, from_=4, to=64, textvariable=length_var, width=5, font=("Arial", 10)).pack(side="left", padx=5)

# Character type options
use_upper = tk.BooleanVar(value=True)
use_lower = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=False)

options_frame = tk.LabelFrame(root, text="Include:", padx=10, pady=10, bg="#ffffff", font=("Arial", 10))
options_frame.pack(pady=10)

tk.Checkbutton(options_frame, text="Uppercase (A-Z)", variable=use_upper, bg="#ffffff").grid(row=0, column=0, sticky="w")
tk.Checkbutton(options_frame, text="Lowercase (a-z)", variable=use_lower, bg="#ffffff").grid(row=1, column=0, sticky="w")
tk.Checkbutton(options_frame, text="Digits (0-9)", variable=use_digits, bg="#ffffff").grid(row=2, column=0, sticky="w")
tk.Checkbutton(options_frame, text="Symbols (!@#...)", variable=use_symbols, bg="#ffffff").grid(row=3, column=0, sticky="w")

# Generate button
generate_btn = tk.Button(root, text="✨ Generate Password", command=generate_password, bg="#88d498", fg="white", font=("Arial", 11, "bold"), width=25)
generate_btn.pack(pady=20)

root.mainloop()

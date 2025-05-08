import tkinter as tk
from tkinter import messagebox
import time
from datetime import datetime


class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock, Timer & Stopwatch")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        # ================== Clock ==================
        self.clock_label = tk.Label(root, text="", font=("Helvetica", 24), fg="blue")
        self.clock_label.pack(pady=10)
        self.update_clock()

        # ================== Timer ==================
        tk.Label(root, text="Timer (seconds):").pack()
        self.timer_entry = tk.Entry(root)
        self.timer_entry.pack()
        self.timer_label = tk.Label(root, text="", font=("Helvetica", 16), fg="red")
        self.timer_label.pack()
        self.timer_running = False
        tk.Button(root, text="Start Timer", command=self.start_timer).pack()

        # ================== Stopwatch ==================
        self.stopwatch_time = 0
        self.stopwatch_running = False

        self.stopwatch_label = tk.Label(root, text="00:00:00", font=("Helvetica", 18), fg="green")
        self.stopwatch_label.pack(pady=10)

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Start", command=self.start_stopwatch).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Stop", command=self.stop_stopwatch).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Reset", command=self.reset_stopwatch).grid(row=0, column=2, padx=5)

    def update_clock(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text=f"Time: {now}")
        self.root.after(1000, self.update_clock)

    def start_timer(self):
        if self.timer_running:
            return
        try:
            seconds = int(self.timer_entry.get())
            self.timer_running = True
            self.countdown(seconds)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")

    def countdown(self, remaining):
        if remaining >= 0 and self.timer_running:
            mins, secs = divmod(remaining, 60)
            self.timer_label.config(text=f"{mins:02}:{secs:02}")
            self.root.after(1000, lambda: self.countdown(remaining - 1))
        else:
            if self.timer_running:
                messagebox.showinfo("Timer", "Time's up!")
            self.timer_running = False

    def start_stopwatch(self):
        if not self.stopwatch_running:
            self.stopwatch_running = True
            self.update_stopwatch()

    def stop_stopwatch(self):
        self.stopwatch_running = False

    def reset_stopwatch(self):
        self.stopwatch_running = False
        self.stopwatch_time = 0
        self.stopwatch_label.config(text="00:00:00")

    def update_stopwatch(self):
        if self.stopwatch_running:
            self.stopwatch_time += 1
            mins, secs = divmod(self.stopwatch_time, 60)
            hrs, mins = divmod(mins, 60)
            self.stopwatch_label.config(text=f"{hrs:02}:{mins:02}:{secs:02}")
            self.root.after(1000, self.update_stopwatch)


if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()

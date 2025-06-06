"""
Feature: History Log
Description:
- Adds a Listbox to store and display past progress attempts.
- Each entry shows the entered time (hh:mm:ss) and percentage completed.
- Adds entry whether timer completes fully or is stopped midway.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time


class ProgressBarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Live Progress Bar with History")
        self.root.geometry("460x400")
        self.root.resizable(False, False)

        self.stop_flag = False
        self.thread = None

        self.setup_ui()

    def setup_ui(self):
        # Main title
        tk.Label(self.root, text="Live Progress Bar Generator", font=("Helvetica", 14, "bold")).pack(pady=10)

        # Frame for time input fields (hours, minutes, seconds)
        time_frame = tk.Frame(self.root)
        time_frame.pack(pady=5)

        self.hours_entry = self._create_time_input(time_frame, "Hours")
        self.minutes_entry = self._create_time_input(time_frame, "Minutes")
        self.seconds_entry = self._create_time_input(time_frame, "Seconds")

        # Main progress bar
        self.progress = ttk.Progressbar(self.root, length=350, mode='determinate', maximum=100)
        self.progress.pack(pady=15)

        # Percentage display label
        self.percent_label = tk.Label(self.root, text="0.00%", font=("Helvetica", 12))
        self.percent_label.pack()

        # Frame for Start and Stop buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        # Start button
        self.start_btn = tk.Button(btn_frame, text="Start", command=self.start_progress)
        self.start_btn.grid(row=0, column=0, padx=10)

        # Stop button (disabled initially)
        self.stop_btn = tk.Button(btn_frame, text="Stop", command=self.stop_progress, state=tk.DISABLED)
        self.stop_btn.grid(row=0, column=1, padx=10)

        # History section label
        tk.Label(self.root, text="History", font=("Helvetica", 12, "bold")).pack(pady=(10, 0))

        # History Listbox with scrollbar
        hist_frame = tk.Frame(self.root)
        hist_frame.pack()

        self.history_listbox = tk.Listbox(hist_frame, height=6, width=50)  # Listbox to show history
        self.history_listbox.pack(side=tk.LEFT, pady=5)

        scrollbar = tk.Scrollbar(hist_frame, orient=tk.VERTICAL, command=self.history_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.history_listbox.config(yscrollcommand=scrollbar.set)

    def _create_time_input(self, parent, label_text):
        # Helper method to create labeled time input field
        frame = tk.Frame(parent)
        frame.pack(side=tk.LEFT, padx=10)
        tk.Label(frame, text=label_text).pack()
        entry = tk.Entry(frame, width=5)
        entry.pack()
        return entry

    def get_total_seconds(self):
        # Converts entered time into total seconds
        try:
            h = int(self.hours_entry.get() or 0)
            m = int(self.minutes_entry.get() or 0)
            s = int(self.seconds_entry.get() or 0)
            total = h * 3600 + m * 60 + s
            if total <= 0:
                raise ValueError
            return total, f"{h:02}:{m:02}:{s:02}"  # Return time in string format too
        except ValueError:
            return None, None

    def start_progress(self):
        # Called when Start button is pressed
        total_seconds, time_str = self.get_total_seconds()
        if total_seconds is None:
            messagebox.showerror("Invalid Input", "Please enter a valid positive time.")
            return

        # Reset states
        self.stop_flag = False
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.progress["value"] = 0
        self.percent_label.config(text="0.00%")

        # Start progress in a separate thread
        self.thread = threading.Thread(target=self.run_progress, args=(total_seconds, time_str), daemon=True)
        self.thread.start()

    def run_progress(self, duration, time_str):
        # Logic to update progress bar over time
        start_time = time.time()
        end_time = start_time + duration

        while not self.stop_flag:
            now = time.time()
            elapsed = now - start_time
            progress = min(elapsed / duration, 1.0)
            percentage = progress * 100

            self.progress["value"] = percentage
            self.percent_label.config(text=f"{percentage:.2f}%")

            if progress >= 1.0:
                break

            time.sleep(0.05)  # Smooth refresh rate

        # Reset button states after completion/stopping
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)

        # Add completed entry to history
        self.add_to_history(time_str, percentage)

    def stop_progress(self):
        # Called when Stop button is pressed
        self.stop_flag = True
        current_val = self.progress["value"]
        self.percent_label.config(text="Stopped")

        _, time_str = self.get_total_seconds()
        self.add_to_history(time_str, current_val)  # Save current progress to history

    def add_to_history(self, time_str, percentage):
        # Adds an entry to the history listbox
        if time_str:
            self.history_listbox.insert(tk.END, f"⏱ {time_str} → {percentage:.2f}%")


if __name__ == "__main__":
    root = tk.Tk()
    app = ProgressBarApp(root)
    root.mainloop()

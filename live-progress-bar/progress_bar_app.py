import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time


class ProgressBarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Live Progress Bar")
        self.root.geometry("420x260")
        self.root.resizable(False, False)

        self.stop_flag = False
        self.thread = None

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Live Progress Bar Generator", font=("Helvetica", 14, "bold")).pack(pady=10)

        # Time Inputs
        time_frame = tk.Frame(self.root)
        time_frame.pack(pady=5)

        self.hours_entry = self._create_time_input(time_frame, "Hours")
        self.minutes_entry = self._create_time_input(time_frame, "Minutes")
        self.seconds_entry = self._create_time_input(time_frame, "Seconds")

        # Progress Bar
        self.progress = ttk.Progressbar(self.root, length=350, mode='determinate', maximum=100)
        self.progress.pack(pady=15)

        # Percentage Label
        self.percent_label = tk.Label(self.root, text="0.00%", font=("Helvetica", 12))
        self.percent_label.pack()

        # Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        self.start_btn = tk.Button(btn_frame, text="Start", command=self.start_progress)
        self.start_btn.grid(row=0, column=0, padx=10)

        self.stop_btn = tk.Button(btn_frame, text="Stop", command=self.stop_progress, state=tk.DISABLED)
        self.stop_btn.grid(row=0, column=1, padx=10)

    def _create_time_input(self, parent, label_text):
        frame = tk.Frame(parent)
        frame.pack(side=tk.LEFT, padx=10)
        tk.Label(frame, text=label_text).pack()
        entry = tk.Entry(frame, width=5)
        entry.pack()
        return entry

    def get_total_seconds(self):
        try:
            h = int(self.hours_entry.get() or 0)
            m = int(self.minutes_entry.get() or 0)
            s = int(self.seconds_entry.get() or 0)
            total = h * 3600 + m * 60 + s
            if total <= 0:
                raise ValueError
            return total
        except ValueError:
            return None

    def start_progress(self):
        total_seconds = self.get_total_seconds()
        if total_seconds is None:
            messagebox.showerror("Invalid Input", "Please enter a valid positive time.")
            return

        self.stop_flag = False
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.progress["value"] = 0
        self.percent_label.config(text="0.00%")

        self.thread = threading.Thread(target=self.run_progress, args=(total_seconds,), daemon=True)
        self.thread.start()

    def run_progress(self, duration):
        start_time = time.time()
        end_time = start_time + duration

        while not self.stop_flag:
            now = time.time()
            elapsed = now - start_time
            progress = min(elapsed / duration, 1.0)  # بین ۰ و ۱
            percentage = progress * 100

            self.progress["value"] = percentage
            self.percent_label.config(text=f"{percentage:.2f}%")

            if progress >= 1.0:
                break

            time.sleep(0.05)  # smoother

        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)

    def stop_progress(self):
        self.stop_flag = True
        self.percent_label.config(text="Stopped")


if __name__ == "__main__":
    root = tk.Tk()
    app = ProgressBarApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import threading
import time

def start_countdown():
    try:
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())
        hour = int(entry_hour.get())
        minute = int(entry_minute.get())

        event_time = datetime(year, month, day, hour, minute)
        now = datetime.now()

        if event_time <= now:
            messagebox.showerror("Invalid Date", "Event time must be in the future!")
            return

        def countdown():
            while True:
                now = datetime.now()
                diff = event_time - now

                if diff.total_seconds() <= 0:
                    lbl_result.config(text="🎉 Event is happening now!")
                    break

                days = diff.days
                hours, remainder = divmod(diff.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)

                lbl_result.config(text=f"{days}d {hours}h {minutes}m {seconds}s remaining")
                time.sleep(1)

        threading.Thread(target=countdown, daemon=True).start()

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers!")

# GUI
root = tk.Tk()
root.title("Event Countdown")
root.geometry("360x300")
root.resizable(False, False)

tk.Label(root, text="Enter Event Date and Time").pack(pady=10)

frame_inputs = tk.Frame(root)
frame_inputs.pack()

tk.Label(frame_inputs, text="Day").grid(row=0, column=0)
tk.Label(frame_inputs, text="Month").grid(row=0, column=1)
tk.Label(frame_inputs, text="Year").grid(row=0, column=2)
tk.Label(frame_inputs, text="Hour").grid(row=0, column=3)
tk.Label(frame_inputs, text="Minute").grid(row=0, column=4)

entry_day = tk.Entry(frame_inputs, width=4)
entry_month = tk.Entry(frame_inputs, width=4)
entry_year = tk.Entry(frame_inputs, width=6)
entry_hour = tk.Entry(frame_inputs, width=4)
entry_minute = tk.Entry(frame_inputs, width=4)

entry_day.grid(row=1, column=0)
entry_month.grid(row=1, column=1)
entry_year.grid(row=1, column=2)
entry_hour.grid(row=1, column=3)
entry_minute.grid(row=1, column=4)

tk.Button(root, text="Start Countdown", command=start_countdown).pack(pady=15)

lbl_result = tk.Label(root, text="", font=("Courier", 14))
lbl_result.pack(pady=20)

root.mainloop()

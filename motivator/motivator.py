import tkinter as tk
import random

# List of 50 motivational quotes
motivational_quotes = [
    "Don't watch the clock; do what it does. Keep going.",
    "Success is the sum of small efforts, repeated day in and day out.",
    "The way to get started is to quit talking and begin doing.",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t just find you. You have to go out and get it.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Dream bigger. Do bigger.",
    "It's going to be hard, but hard does not mean impossible.",
    "Don't stop when you're tired. Stop when you're done.",
    "Wake up with determination. Go to bed with satisfaction.",
    "Do something today that your future self will thank you for.",
    "Little things make big days.",
    "It's never too late to be what you might have been.",
    "Believe you can and you're halfway there.",
    "The only way to achieve the impossible is to believe it is possible.",
    "Success is not how high you have climbed, but how you make a positive difference to the world.",
    "Start where you are. Use what you have. Do what you can.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Hardships often prepare ordinary people for an extraordinary destiny.",
    "Don't wait for opportunity. Create it.",
    "Success is not in what you have, but who you are.",
    "You are braver than you believe, stronger than you seem, and smarter than you think.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Everything you can imagine is real.",
    "It always seems impossible until it's done.",
    "If you can dream it, you can do it.",
    "The secret of getting ahead is getting started.",
    "Believe in yourself and all that you are.",
    "The best way to predict the future is to create it.",
    "What you get by achieving your goals is not as important as what you become by achieving your goals.",
    "In the middle of every difficulty lies opportunity.",
    "A goal without a plan is just a wish.",
    "You are never too old to set another goal or to dream a new dream.",
    "The road to success and the road to failure are almost exactly the same.",
    "Opportunities don't happen, you create them.",
    "Success usually comes to those who are too busy to be looking for it.",
    "The way to get started is to quit talking and begin doing.",
    "I am not a product of my circumstances. I am a product of my decisions.",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
    "Act as if what you do makes a difference. It does.",
    "The only place where success comes before work is in the dictionary.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The best revenge is massive success.",
    "Your time is limited, so don’t waste it living someone else’s life.",
    "In order to succeed, we must first believe that we can.",
    "What you do today can improve all your tomorrows.",
    "I find that the harder I work, the more luck I seem to have."
]

# Function to display motivational quote of the day
def show_motivational_quote():
    # Randomly choose a quote from the list
    quote = random.choice(motivational_quotes)
    # Update the label with the selected quote
    quote_label.config(text=quote)

# Function to mark task as completed and show the next quote
def task_completed():
    # Display the checkmark symbol to indicate task completion
    checkmark_label.config(text="✔️ Task Completed!")
    # Show the next motivational quote
    show_motivational_quote()

# Design the user interface with Tkinter
root = tk.Tk()
root.title("Daily Motivation")

# Label to display the motivational quote
quote_label = tk.Label(root, text="", font=("Helvetica", 14), wraplength=400)
quote_label.pack(pady=20)

# Button to mark the task as completed
task_button = tk.Button(root, text="Done Task", command=task_completed, font=("Helvetica", 12))
task_button.pack(pady=10)

# Label to show the checkmark after task completion
checkmark_label = tk.Label(root, text="", font=("Helvetica", 12))
checkmark_label.pack(pady=10)

# Display the first motivational quote
show_motivational_quote()

# Start the Tkinter event loop
root.mainloop()

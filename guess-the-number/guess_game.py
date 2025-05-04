import random
import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    slow_print("🤖 I've picked a number between 1 and 100. Try to guess it!")

    while True:
        user_input = input("👉 Your guess (or 'q' to quit): ").strip().lower()

        if user_input == 'q':
            slow_print("👋 Alright, quitting the game. See you next time!")
            return False  # user wants to quit

        if not user_input.isdigit():
            slow_print("⛔ Please enter a valid number.")
            continue

        guess = int(user_input)
        attempts += 1

        if guess < number:
            slow_print("⬆️ Higher...")
        elif guess > number:
            slow_print("⬇️ Lower...")
        else:
            slow_print(f"🎉 Boom! The number was {number}.")
            slow_print(f"✅ You guessed it in {attempts} attempts.")
            if attempts <= 5:
                slow_print("🔥 Genius level!")
            elif attempts <= 10:
                slow_print("👏 Good job!")
            else:
                slow_print("😅 Took some effort, huh?")
            return True  # user finished a round

def guess_game():
    slow_print("🎮 Welcome to the Number Guessing Game!")
    while True:
        game_result = play_game()
        if not game_result:
            break
        slow_print("\n🔁 Starting a new round...\n")

if __name__ == "__main__":
    guess_game()

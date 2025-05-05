import random

def slow_print(text, delay=0.03):
    import sys, time
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return "player"
    else:
        return "computer"

# Global win counters for stats
total_player_wins = 0
total_computer_wins = 0

slow_print("🎮 Welcome to Rock, Paper, Scissors!")
slow_print("First to 5 wins per match. Type 'q' anytime to quit.\n")

while True:
    player_score = 0
    computer_score = 0

    while player_score < 5 and computer_score < 5:
        user = input("Choose (rock/paper/scissors): ").lower()
        if user == 'q':
            slow_print("❗ Game exited early.")
            break
        if user not in ['rock', 'paper', 'scissors']:
            print("❌ Invalid choice. Try again.")
            continue

        computer = get_computer_choice()
        slow_print(f"💻 Computer chose: {computer}")
        result = determine_winner(user, computer)

        if result == "player":
            player_score += 1
            slow_print("✅ You win this round!")
        elif result == "computer":
            computer_score += 1
            slow_print("❌ Computer wins this round!")
        else:
            slow_print("➖ It's a tie!")

        print(f"🏆 Current Score - You: {player_score} | Computer: {computer_score}\n")

    # End of match logic
    if player_score == 5:
        slow_print("🎉 You won this match!\n")
        total_player_wins += 1
    elif computer_score == 5:
        slow_print("💀 Computer won this match!\n")
        total_computer_wins += 1

    print(f"📊 Total Matches Won - You: {total_player_wins} | Computer: {total_computer_wins}")
    again = input("🔁 Play another match? (y/n): ").lower()
    if again == 'q' or again == 'n':
        slow_print("👋 Thanks for playing! Goodbye!")
        break

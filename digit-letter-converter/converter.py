# Digit Wordifier v2.1 - Continuous Mode
# Author: voidcompile

import itertools

digit_to_letters = {
    '1': ['a', 'b', 'c'],
    '2': ['d', 'e', 'f'],
    '3': ['g', 'h', 'i'],
    '4': ['j', 'k', 'l'],
    '5': ['m', 'n', 'o'],
    '6': ['p', 'q', 'r'],
    '7': ['s', 't', 'u'],
    '8': ['v', 'w'],
    '9': ['x', 'y'],
    '0': ['z']
}

# Reverse mapping
letter_to_digit = {letter: digit for digit, letters in digit_to_letters.items() for letter in letters}

def get_char_lists(digits):
    char_lists = []
    for d in digits:
        if d in digit_to_letters:
            char_lists.append(digit_to_letters[d])
        else:
            print(f"⚠️ Skipping invalid character: '{d}'")
    return char_lists

def generate_words(digits):
    char_lists = get_char_lists(digits)
    combos = itertools.product(*char_lists)
    return [''.join(c) for c in combos]

def save_words(words, filename="output_words.txt"):
    with open(filename, "w") as f:
        for word in words:
            f.write(word + "\n")
    print(f"\n✅ Saved {len(words)} words to '{filename}'")

def encode_word_to_digits(word):
    """Convert a word to its digit representation based on letter_to_digit."""
    word = word.lower()
    digits = ''
    for ch in word:
        if ch in letter_to_digit:
            digits += letter_to_digit[ch]
        else:
            print(f"⚠️ Skipping unsupported character: '{ch}'")
    return digits

def main():
    print("🔤 Digit Wordifier v2.1 (With Reverse Encoder - Continuous Mode)\n")
    
    while True:
        print("\nChoose mode: [1] Number → Words  |  [2] Word → Number  |  [q] Quit")
        mode = input("Your choice: ").strip().lower()

        if mode == '1':
            digits = input("Enter a number (e.g., 420): ")
            words = generate_words(digits)
            print("\n✨ First 10 generated words:")
            print(words[:10])
            save_words(words)
        
        elif mode == '2':
            word = input("Enter a word (e.g., alex): ")
            number = encode_word_to_digits(word)
            print(f"\n🔁 Digit representation of '{word}': {number}")

        elif mode == 'q':
            print("\n👋 Exiting the program. See you again!")
            break
        
        else:
            print("❌ Invalid mode. Please try again.")

if __name__ == "__main__":
    main()

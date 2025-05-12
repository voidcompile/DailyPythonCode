from collections import Counter

def count_characters(text):
    # Count the occurrences of each character in the text
    return Counter(text)

def display_count(count_dict):
    # Display the character count in a tabular format
    print(f"{'Character':<15}{'Count'}")
    print("="*30)
    for char, count in count_dict.items():
        # Check if the character is a number and display it properly
        print(f"{repr(char):<15}{count}")

def main():
    text = input("Enter a text: ")
    # Count the characters in the input text
    count_dict = count_characters(text)
    # Display the count of characters
    display_count(count_dict)

if __name__ == "__main__":
    main()

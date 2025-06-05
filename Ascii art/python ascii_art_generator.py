import pyfiglet

def ascii_art_generator():
    text = input("Enter the text to convert to ASCII Art: ")
    ascii_art = pyfiglet.figlet_format(text)
    print("\nHere is your ASCII Art:\n")
    print(ascii_art)

if __name__ == "__main__":
    ascii_art_generator()

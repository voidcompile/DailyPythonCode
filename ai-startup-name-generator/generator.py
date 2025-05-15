import random

prefixes = ["Hyper", "Smart", "Quick", "Eco", "Bright", "Auto", "Next", "Blue"]
suffixes = ["ly", "ify", "scape", "gen", "loop", "mate", "hub", "zone"]

def generate_startup_names(base_word, count=5):
    names = []
    for _ in range(count):
        prefix = random.choice(prefixes)
        suffix = random.choice(suffixes)
        name = f"{prefix}{base_word.capitalize()}{suffix}"
        names.append(name)
    return names

def main():
    print("🚀 AI Startup Name Generator")
    base = input("🔤 Enter a base word (e.g., 'data', 'food', 'tech'): ").strip()
    results = generate_startup_names(base)
    print("\n✨ Here are your startup name ideas:\n")
    for name in results:
        print(f" - {name}")

if __name__ == "__main__":
    main()

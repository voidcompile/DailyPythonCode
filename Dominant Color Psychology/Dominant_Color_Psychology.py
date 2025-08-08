from PIL import Image
import sys
from collections import Counter

# Psychological meaning for major colors
color_meanings = {
    "red": "Energy, passion, urgency, and sometimes danger.",
    "blue": "Calmness, trust, relaxation, and stability.",
    "green": "Nature, balance, freshness, and growth.",
    "yellow": "Happiness, optimism, attention, and creativity.",
    "orange": "Warmth, enthusiasm, friendliness, and excitement.",
    "purple": "Luxury, mystery, spirituality, and imagination.",
    "black": "Power, sophistication, elegance, and sometimes fear.",
    "white": "Purity, simplicity, peace, and cleanliness."
}

# Function to classify RGB to a basic color name
def get_color_name(rgb):
    r, g, b = rgb
    if r > 200 and g < 100 and b < 100:
        return "red"
    elif r < 100 and g < 100 and b > 200:
        return "blue"
    elif r < 100 and g > 200 and b < 100:
        return "green"
    elif r > 200 and g > 200 and b < 100:
        return "yellow"
    elif r > 200 and g > 100 and b < 100:
        return "orange"
    elif r > 100 and b > 100 and g < 100:
        return "purple"
    elif r < 50 and g < 50 and b < 50:
        return "black"
    elif r > 200 and g > 200 and b > 200:
        return "white"
    else:
        return "unknown"

# Main program
if len(sys.argv) < 2:
    print("Usage: python color_psychology.py <image_path>")
    sys.exit(1)

image_path = sys.argv[1]
image = Image.open(image_path)
image = image.resize((50, 50))  # Reduce size for faster processing
pixels = list(image.getdata())

# Find the most common color
most_common_rgb = Counter(pixels).most_common(1)[0][0]

# Get color name & meaning
color_name = get_color_name(most_common_rgb)
meaning = color_meanings.get(color_name, "No meaning found for this color.")

print(f"Dominant Color RGB: {most_common_rgb}")
print(f"Detected Color Name: {color_name}")
print(f"Psychological Meaning: {meaning}")

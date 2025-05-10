# 🔢↔️🔤 Digit-Letter Converter

A simple yet powerful Python tool for converting **digits to letter combinations** (like a classic mobile keypad) and **words back to digits**. Useful for coding exercises, basic cryptography, and understanding data encoding concepts.

---

## 🚀 Features

- Convert a **number** into all possible **letter combinations**.
- Convert a **word** back into its corresponding **digit code**.
- Loop-based user interaction – use as long as you want.
- Fully built with Python standard libraries – no external dependencies.

---

## 🔄 Conversion Logic

### 1. Number ➝ Letters (Word Generation)

Each digit maps to multiple possible characters based on a custom mapping inspired by old mobile keypads.

Example:
1 → ['a', 'b', 'c']
2 → ['d', 'e', 'f']
3 → ['g', 'h', 'i']
...


Input like:
12 ➝ ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']


### 2. Word ➝ Number (Encoding)

Each letter is mapped back to a single digit. This mapping is **one-way and lossy** – you cannot reverse it to get all original letters.

Example:
a → 1, d → 2, g → 3, ..., z → 0
dog ➝ 235


---

## ⚠️ Important Notes

- The **forward conversion (digits ➝ letters)** is **multi-output**, generating all possible combinations.
- The **reverse conversion (letters ➝ digits)** is **one-to-one**, meaning data loss is possible in reverse lookup.

---

## 🧪 Sample Usage


Enter a number or a word:

23

Possible letter combinations:

gd

ge

gf

hd
...

Enter a number or a word:

cat

Digit code: 145

yaml
Copy
Edit


---

## 💡 Future Ideas

- GUI version with Tkinter  
- Web API using Flask or FastAPI  
- Encode/Decode mode toggle  
- Add support for custom mapping sets  

---

## 🧠 License & Author

Open-source project by @voidcompile  
MIT License. Contributions are welcome!

---

## 💻 voidcompile

Stay updated with daily Python & AI projects on our channel:
📢 [github: @voidcompile](https://github.com/voidcompile)
📢 [Telegram: @voidcompile](https://t.me/voidcompile)
📢 [youtube: @voidcompile](https://www.youtube.com/@voidcompile)
📢 [email: voidcompile@gmail.com]




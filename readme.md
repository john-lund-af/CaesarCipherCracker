

# CaesarCipherCracker

A simple **Caesar Cipher cracker** implemented in **Python**.

This project brute-forces every possible shift key for a given alphabet  
(default: **Swedish alphabet** `A–ZÅÄÖ`) and ranks the results using a small
Swedish common-words lexicon to suggest the **most probable plaintext**.

---

## 🚀 Features

- Brute-force decryption of Caesar cipher
- Supports custom alphabets (default: Swedish alphabet)
- Scores decrypted candidates using a Swedish word lexicon
- Displays:
  - All possible decryptions
  - The most probable plaintext

---

## 📂 Project Structure

```

CaesarCipherCracker/
│
├── main.py           # CLI entry point
├── cipher_utils.py   # Core cipher logic
├── .gitignore
└── README.md

````

### main.py

- Reads encrypted input from the user
- Generates all possible decryptions
- Scores each candidate
- Prints the most probable result

### cipher_utils.py

Contains:

- `decrypt(message, key, symbols)`  
  Decrypts a message using a specific key.

- `decryption_candidates(text, symbols)`  
  Generates all possible decryptions.

- `evaluate_decryption(text, common_words)`  
  Scores a decrypted message based on word matches.

---

## 🐍 Requirements

- Python **3.10+**
- No external dependencies required

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/john-lund-af/CaesarCipherCracker.git
cd CaesarCipherCracker
````

Run the program:

```bash
python3 main.py
```

You will see:

```
Encrypted Caesar Cipher Message:
>
```

Paste your encrypted message and press Enter.

The program will:

1. Print every candidate decryption
2. Display the most probable result

---

## 🔤 Customization

### Change Alphabet

Inside `main.py`:

```python
SWEDISH_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
```

To use English only:

```python
ENGLISH_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
```

The cracker will try one key per symbol in the alphabet.

---

### Improve Scoring

Expand the `SWEDISH_WORDS` set in `main.py`
to improve detection accuracy.

More words = better scoring.

---

## ⚠️ Limitations

* Caesar cipher is cryptographically weak.
* Short messages may produce ambiguous results.
* Scoring is based on a small word list.
* Unusual vocabulary may lower accuracy.

---

## 💡 Possible Improvements

* Add unit tests
* Add encryption functionality
* Add command-line arguments
* Improve scoring using frequency analysis or n-grams
* Add support for multiple languages

---

## 📚 Educational Purpose

This project was built as part of learning:

* Python functions
* Dictionaries & sets
* Type hints
* Modular programming
* CLI interaction
* Basic cryptography concepts

---

## 📝 License

This project is for educational purposes.
Feel free to modify and improve.

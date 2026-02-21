# Logiken
# Istället för att be användaren om en nyckel, ska ditt program:
# 1. Ta emot ett krypterat meddelande.
# 2. Loopa igenom alla möjliga nycklar (från 0 till längden av SYMBOLS ).
# 3. För varje nyckel, anropa din befintliga funktion translate_message i läget "decrypt".
# 4. Skriva ut resultatet för varje försök så att en människa kan läsa och se när texten blir
# begriplig.

from cipher_utils import decryption_candidates

SWEDISH_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"

if __name__ == "__main__":

    print("Encrypted Caesar Cipher Message:")
    cc_msg = input("> ")

    candidates = decryption_candidates(cc_msg, SWEDISH_ALPHABET)
    for key, text in candidates:
        print(f"Key: {key}, Text: {text}")


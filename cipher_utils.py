
def decrypt(cc_message: str, key: int, symbols: str) -> str:
    """
    Decrypts a Caesar Cipher message by changing each letter position by subtracting with given key
    :param cc_message: A string containing the Caesar cipher message
    :param key: Key that was used to encrypt the message
    :param symbols: A string containing the symbols to use to decipher the message (e.g. english alphabet)
    :return: Decrypted message
    """

    decrypted_chs: list[str] = [] # List for decrypted characters
    cc_message = cc_message.casefold()
    symbols = symbols.casefold()

    for ch in cc_message:
        # Just adds the character to the decrypted_chs list if the character is not included in symbols str.
        if ch.casefold() not in symbols.casefold():
            decrypted_chs.append(ch)
            continue

        position: int = symbols.find(ch.casefold()) - key

        if position < 0:
            position = len(symbols) + position

        ch = symbols[position]
        decrypted_chs.append(ch)

    return "".join(decrypted_chs)


def decryption_candidates(text: str, symbols: str) -> list[dict]:
    """
    Returns all possible combinations of the given text
    :param text: The encrypted text
    :param symbols: The symbols used for encrypting the text
    :return: A list of dictionaries where each dict contains a key and a text candidate.
    """
    candidates = []

    for key in range(len(symbols)):
        candidate = decrypt(text, key, symbols)
        if candidate != text:
            candidates.append({"key" : key, "text": candidate})

    return candidates


def evaluate_decryption(text: str, common_words: set) -> int:
    """
    Returns the number of encountered words in the common_words set.
    :param text: A string with the text to evaluate
    :param common_words: A set with common words used to evaluate the text.
    :return: An integer with the number of encountered words in the common_words set
    """
    word_set = set(text.split())
    new_set = common_words.intersection(word_set)
    return len(new_set)

def decrypt(cc_message: str, key: int, symbols: str) -> str:
    """
    Decrypts a Caesar Cipher message
    :param cc_message: A string containing the Caesar cipher message
    :param key: Key that was used to encrypt the message
    :param symbols: A string containing the symbols to use to decipher the message (e.g. english alphabet)
    :return: Decrypted message
    """

    decrypted_chs: list[str] = [] # List for decrypted characters

    for ch in cc_message:
        # Just adds the character to the decrypted_chs list if the character is not part of the swedish alphabet
        if ch.casefold() not in symbols:
            decrypted_chs.append(ch)
            continue

        position: int = symbols.find(ch.casefold()) - key

        if position < 0:
            position = len(symbols) + position

        ch = symbols[position]
        decrypted_chs.append(ch)

    return "".join(decrypted_chs)

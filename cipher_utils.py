
SWEDISH_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ".casefold()


def decrypt(cc_message: str, key: int) -> str:
    """
    Decrypts a Caesar Cipher message
    :param cc_message: A string containing the Caesar cipher message
    :param key: Key that was used to encrypt the message
    :return: Decrypted message
    """

    decrypted_chs: list[str] = [] # List for decrypted characters

    for ch in cc_message:
        # Just adds the character to the decrypted_chs list if the character is not part of the swedish alphabet
        if ch.casefold() not in SWEDISH_ALPHABET:
            decrypted_chs.append(ch)
            continue

        position: int = SWEDISH_ALPHABET.find(ch.casefold()) - key

        if position < 0:
            position = len(SWEDISH_ALPHABET) + position

        ch = SWEDISH_ALPHABET[position]
        decrypted_chs.append(ch)

    return "".join(decrypted_chs)
def rotate(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    Upper_alphabet = alphabet.upper()
    encoded_text = ''
    for i in range(0,len(text)):
        if not text[i].isalpha():
            encoded_text += text[i]
            continue 
        if text[i].isupper():
            caesar_shift = (Upper_alphabet.index(text[i]) + key) % 26
            encoded_text += Upper_alphabet[caesar_shift]
            continue

        caesar_shift = (alphabet.index(text[i]) + key) % 26
        encoded_text += alphabet[caesar_shift]

    return encoded_text
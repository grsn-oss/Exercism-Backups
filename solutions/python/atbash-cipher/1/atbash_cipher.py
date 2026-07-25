def encode(plain_text):
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    encrypted = ""
    space = 0
    true_encrypted = ""
    for char in plain_text.lower():
        if char.isdigit():
            encrypted += char
        if char.isalpha() == False:
            encrypted += ""
        else:
            encrypted += cipher[plain.index(char)]

    for char2 in encrypted:
        true_encrypted += char2
        space += 1

        if space == 5:
            true_encrypted += " "
            space = 0
        
    return(true_encrypted.strip())
def decode(ciphered_text):
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    decrypted = ""
    for char in ciphered_text:
        if char.isspace() or char in ".,":
            decrypted += ""
        elif char.isdigit():
            decrypted += char
        else:
            decrypted += plain[cipher.index(char)] 
    return(decrypted)

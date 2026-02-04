def is_isogram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_string = string.lower()
    for index in range(0,len(alphabet)):
        if new_string.count(alphabet[index]) > 1:
            return False

    return True

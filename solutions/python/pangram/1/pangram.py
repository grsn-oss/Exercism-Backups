def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # new_sentence = sentence.lower()
    letter_sum = 0
    new_s = sentence.lower()
    for index in range(0,len(alphabet)):
        if alphabet[index] in new_s:
            letter_sum+=1

    if letter_sum == 26:
        return True

    return False

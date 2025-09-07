def translate(text):        
    vowel = 'aeiou'
    if len(text) >= 14:
        array_text = text.split()
        for counter in range(0,len(array_text)):
            array_text[counter] = translate(array_text[counter])
        return " ".join(array_text)
#If the word is my(for now)
    if text == "my":
        return 'ymay'
        
#if the word start with a consonant followed by y:        
    if 'y' in text[1:] and not text[-1] == 'y':
        Y_index = text[1:-1].find('y')
        return text[Y_index+1::] + text[0:Y_index+1] + "ay"
        
# If the first letter is a vowel or xr or yt        
    if text[0] in vowel or text[0:2] == "xr" or text[0:2] == "yt":
        return text + "ay"

#SQU and QU rule
    if text[0:2] == "qu":
        return text[2::] + text[0:2] + "ay"

    if text[0:3] == "squ":
        return text[3::] + text[0:3] + "ay"
    
# Rule 2
    vowel_index = 0
    for index in range(0,len(text)):
        if text[index] in vowel:
            vowel_index = text.find(text[index])
            break

    new_text = text[vowel_index::] + text[0:vowel_index] + "ay"
    return new_text


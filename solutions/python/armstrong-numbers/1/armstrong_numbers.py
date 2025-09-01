def is_armstrong_number(number):
    int_str = str(number)                     #Transform the number into a string to iterate
    exp = len(int_str)                        #Exponent taken from the length of the string
    arm_number = 0                            #Armstrong Number
    
    for x in range (0,exp):
        arm_number += int(int_str[x]) ** exp

    if arm_number == number:
        return True 

    return False

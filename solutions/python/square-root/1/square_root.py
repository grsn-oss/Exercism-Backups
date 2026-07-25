def square_root(number):

    result = 0
    prime = 1
    while number > 0:
        number = number - prime
        prime += 2
        result += 1
    return result 

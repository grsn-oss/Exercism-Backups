
def square(number):

    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    grains = 1
    square = 1
    if number == 1:
        return grains
    else:
        for x in range (1,number):
            grains *= 2
    return grains
    
def total():
    total_grains = 0 
    for counter in range(1,65):
        total_grains += square(counter)

    return total_grains

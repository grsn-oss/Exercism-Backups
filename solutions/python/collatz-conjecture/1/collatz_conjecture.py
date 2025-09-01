def steps(number):
    step = 0
    # If the number is negative
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    for counter in range (1,200):
        #Check if the number is even
        if number == 1:
            break
        if number % 2 == 0:
            number = number / 2
        else:
            number = (number * 3) + 1
        # Add 1 to step
        step += 1
        
    return step


def egg_count(display_value):
    actual_value = 0
    res = ' '
    while display_value > 0:
        res = str(display_value & 1) +res
        display_value >>=1

    for x in res:
        if x == "1":
            actual_value +=1

    return actual_value

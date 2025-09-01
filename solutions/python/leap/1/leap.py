def leap_year(year):
    if year % 4 == 0 and not (year % 400 == 0) and year % 100 == 0:      #Skip every century that is not divisible by 400 but by 4
        return False
    if year % 400 == 0 and year % 100 == 0:                              #Every century that is divisible by 400 is a leap year
        return True
    if year % 4 == 0:                                                    #Every 4 years is a leap year
        return True

    else:
        return False                                                 

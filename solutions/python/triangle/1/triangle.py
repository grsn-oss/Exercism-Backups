def is_it_triangle(sides):
    if 0 in sides:
        return False
    if (sides[0] + sides[1] >= sides[2]) and (sides[1] + sides[2] >= sides[0]) and (sides[0] + sides[2] >= sides[1]):
        return True
    return False
def equilateral(sides):
    if is_it_triangle(sides) == False:
        return False

    if sides[0] == sides[1] and sides[1] == sides[2]:
        return True

    return False
    
def isosceles(sides):
    if is_it_triangle(sides) == False:
        return False

    condition_1 = (sides[1] == sides[2]) 
    condition_2 = (sides[0] == sides[2])
    condition_3 = (sides[0] == sides[1])

    if condition_1 or condition_2 or condition_3:
        return True
    return False


def scalene(sides):
    if is_it_triangle(sides) == False:
        return False

    if equilateral(sides) or isosceles(sides):
        return False
    return True
    

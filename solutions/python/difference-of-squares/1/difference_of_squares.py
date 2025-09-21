def square_of_sum(number):
    total_sum = 0
    for counter in range(1,number+1):
        total_sum += counter

    return (total_sum ** 2)


def sum_of_squares(num):

    return (num * (num + 1) * (2 * num + 1)) // 6


def difference_of_squares(number):

    return square_of_sum(number) - sum_of_squares(number)

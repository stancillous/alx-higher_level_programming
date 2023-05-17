#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total = 0
    divisor = 0

    for i in my_list:
        total += i[0] * i[1]
        divisor += i[1]

    return (total / divisor)

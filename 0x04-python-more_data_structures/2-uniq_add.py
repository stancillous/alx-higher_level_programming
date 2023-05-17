#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    new = set(my_list)
    print(new)
    for num in new:
        sum += num
    return (sum)

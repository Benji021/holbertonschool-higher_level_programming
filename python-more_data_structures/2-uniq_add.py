#!/usr/bin/python3
def uniq_add(my_list=[]):
    seen = set()
    total = 0
    for number in my_list:
        if number not in seen:
            seen.add(number)
            total += number
        return total

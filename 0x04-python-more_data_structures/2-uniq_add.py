#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_list = []

    for i in my_list:
        if i not in unique_list:
            unique_list.append(i)
    num = 0
    for x in unique_list:
        num = num + x
    return num

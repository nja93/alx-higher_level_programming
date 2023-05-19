#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    totalsum = []
    totalweight = 0

    for score, weight in my_list:
        totalsum.append(score * weight)
        totalweight += weight
    weight_average = sum(totalsum) / totalweight
    return weight_average

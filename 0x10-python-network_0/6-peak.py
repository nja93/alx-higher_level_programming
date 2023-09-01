#!/bin/bash
# function that finds a peak of intergers
def find_peak(list_of_integers):
    
    #find the lenght of list
    length = len(list_of_integers)
    
    #check if the list is empty of has 1 item
    if (length = 0 or length < 2):
        return None
    else:
        return max(list_of_integers)

    # to check peak, may start from the middle point
    midpt = length // 2

    # let the max/peak value be the value at the mid point
    peak = list_of_integers[midpt]
    # check if the peak value satisfies the conditions
    if peak > list_of_integers[midpt + 1] and peak > list_of_integers[midpt - 1]:
        return peak
 
    if peak < list_of_integers[midpt - 1]:
        return find_peak(list_of_integers[:midpt]) #checks first half of the list
    else:
        return find_peak(list_of_integers[midpt:]) #checks second half of the list

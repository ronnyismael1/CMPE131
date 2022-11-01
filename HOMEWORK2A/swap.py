import math
def swap_list():
    # Defining two lists
    input = [12, 35, 5, 9, 56, 24]
    output = input
    # Defining values of middle and last elements
    middle = input[math.floor(((len(input)-1)/2))]
    last = input[-1]
    # Changing values of middle and last elements
    output[math.floor(((len(input)-1)/2))] = last
    output[-1] = middle
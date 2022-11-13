import math
def swap_list(x):
    output = x
    middle = x[math.floor(((len(x)-1)/2))]
    last = x[-1]
    output[math.floor(((len(x)-1)/2))] = last
    output[-1] = middle
    return output

def sort_dictionary():
    input = {'Tom' : (5464512, 24),
             'Sara' : (5446987, 32),
             'Mary' : (1557896,20)}
    output = {}
    output = sorted(input.values(), key=lambda x: x[1])
        
    print (output.key())
sort_dictionary()
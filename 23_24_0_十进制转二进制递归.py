def bin_1(x):
    if x != 1:
        return str('%s%s' % (bin_1(x//2),  x%2))
    else:
        return str('0b1')
    

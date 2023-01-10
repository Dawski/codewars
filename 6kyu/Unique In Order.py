# Implement the function unique_in_order which takes as argument a sequence
# and returns a list of items without any elements with the same value next to each other
# and preserving the original order of elements.
#
# For example:
#
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

# my solution

import itertools

# The operation of groupby() generates a break
# or new group every time the value of the key function changes

def unique_in_order(iterable):
    return [c for c,k in itertools.groupby(iterable)]

# solutions from cw

def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result

def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return re
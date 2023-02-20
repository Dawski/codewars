# Define a function that takes in two non-negative integers a and b and returns the last decimal digit of
# a b. Note that a and b may be very large!

# My solution

def last_digit(n1, n2):
    if n2 == 0:
        return 1
    elif list(map(int, str(n1)))[-1] == 4 and n2 % 2 == 0:
        return 6
    elif list(map(int, str(n1)))[-1] == 4 and n2 % 2 == 1:
        return 4
    elif list(map(int, str(n1)))[-1] == 9 and n2 % 2 == 0:
        return 1
    elif list(map(int, str(n1)))[-1] == 9 and n2 % 2 == 1:
        return 9
    elif list(map(int, str(n1)))[-1] == 2:
        if n2 % 4 == 0:
            return 6
        elif n2 % 4 == 1:
            return 2
        elif n2 % 4 == 2:
            return 4
        elif n2 % 4 == 3:
            return 8
    elif list(map(int, str(n1)))[-1] == 3:
        if n2 % 4 == 0:
            return 6
        elif n2 % 4 == 1:
            return 3
        elif n2 % 4 == 2:
            return 9
        elif n2 % 4 == 3:
            return 7
    elif list(map(int, str(n1)))[-1] == 7:
        if n2 % 4 == 0:
            return 1
        elif n2 % 4 == 1:
            return 7
        elif n2 % 4 == 2:
            return 9
        elif n2 % 4 == 3:
            return 3
    elif list(map(int, str(n1)))[-1] == 8:
        if n2 % 4 == 0:
            return 6
        elif n2 % 4 == 1:
            return 8
        elif n2 % 4 == 2:
            return 4
        elif n2 % 4 == 3:
            return 2

    my_dict = {
        0: 0,
        1: 1,
        5: 5,
        6: 6,
    }
    return my_dict.get(list(map(int, str(n1)))[-1])



print(last_digit(102,18))


# code wars soutions

def last_digit(n1, n2):
    return pow( n1, n2, 10 )

##########################

import gmpy2

def last_digit(n1, n2):
    return int(str(gmpy2.powmod(n1, n2, 10))[-1:]) if n1 > 0 else 1
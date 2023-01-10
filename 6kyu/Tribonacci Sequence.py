
# n = 5
#
# a = -1
# b = 1
# c = a + b
#
# for i in range(0,n):
#     print(c)
#     a = b
#     b = c
#     c = a + b

# So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:
#
# [1, 1 ,1, 3, 5, 9, 17, 31, ...]
# But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically
# shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence
# shifted by 2 places, but that is not the case and we would get:
#
# [0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
# Well, you may have guessed it by now, but to be clear:
# you need to create a fibonacci function that given a signature array/list,
# returns the first n elements - signature included of the so seeded sequence.

# my solution

def tribonacci(signature, n):
    a = signature[0]
    b = signature[1]
    c = signature[2]
    d = a + b + c
    tribonacci_sequence = signature

    if n == 1:
        tribonacci_sequence = [signature[0]]
    elif n == 2:
        tribonacci_sequence = [signature[0], signature[1]]
    elif n == 0:
        tribonacci_sequence = []
    else:
        for i in range(0, n - 3):
            a = b
            b = c
            c = d
            tribonacci_sequence.append(d)
            d = a + b + c

    return tribonacci_sequence

# solutions for cw

def tribonacci(s, n):
    for i in range(3, n): s.append(s[i-1] + s[i-2] + s[i-3])
    return s[:n]


def tribonacci(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))

    return signature[:n]



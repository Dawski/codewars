# The Collatz conjecture (also known as 3n+1 conjecture) is a conjecture that applying the following algorithm
# to any number we will always eventually reach one:
#
# [This is writen in pseudocode]
# if(number is even) number = number / 2
# if(number is odd) number = 3*number + 1
# #Task
#
# Your task is to make a function hotpo that takes a positive n as input and returns
# the number of times you need to perform this algorithm to get n = 1.

# My solution

def hotpo(n):
    number = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            number += 1
        elif n % 2 != 0:
            n = n*3+1
            number += 1
    return number

# cw solutions

def hotpo(n):
    cnt = 0
    while n != 1:
        n = 3 * n + 1 if n % 2 else n / 2
        cnt += 1
    return cnt

def hotpo(num, count=0):
  return count if num == 1 else hotpo(num / 2 if num % 2 == 0 else num * 3 + 1 ,count + 1)

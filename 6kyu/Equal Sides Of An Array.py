# You are going to be given an array of integers.
# Your job is to take that array and find an index N where the sum of the integers to the left of N
# is equal to the sum of the integers to the right of N.
# If there is no index that would make this happen, return -1.

#my solution

def find_even_index(arr):
    left = []
    right = []
    for i in range(len(arr)):
        left = sum(arr[0:i])
        right = sum(arr[i+1:len(arr)])
        if right == left:
            return i
    return -1

print(find_even_index([10,-80,10,10,15,35,20]))


# cw solutions

def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1


def find_even_index(lst):
    left_sum = 0
    right_sum = sum(lst)
    for i, a in enumerate(lst):
        right_sum -= a
        if left_sum == right_sum:
            return i
        left_sum += a
    return -1
# The main idea is to count all the occurring characters
# in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
#
# What if the string is empty? Then the result should be empty object literal, {}.

#My solution

def count(string):
    b = {}
    for character in string:
        if character not in b.keys():
            b[character] = (string.count(character))
    return b

print(count('dupa'))


#Solution from CW


### 1

from collections import Counter

def count(string):
    return Counter(string)

### 2

def count(s):
    return {x:s.count(x) for x in set(s)}

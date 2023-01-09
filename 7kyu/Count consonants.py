# Write a function consonantCount, consonant_count or ConsonantCount that takes a string of
# English-language text and returns the number of consonants in the string.
#
# Consonants are all letters used to write English excluding the vowels a, e, i, o, u.

# my solution

def consonant_count(s):
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    number_of_consonants = 0
    for letter in s:
        if letter in consonants:
            number_of_consonants += 1
    return number_of_consonants

# solutin from cw

def consonant_count(s):
    vowels = 'aeiou'
    counter = 0
    for letter in s.lower():
        if (letter not in vowels) and letter.isalpha():
            counter += 1
    return counter

# solutin from cw

def consonant_count(str):
    return sum(1 for c in str if c.isalpha() and c.lower() not in "aeiou")
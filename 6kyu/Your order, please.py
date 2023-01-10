# Your task is to sort a given string. Each word in the
# string will contain a single number. This number is the position the word should have in the result.
#
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
#
# If the input string is empty, return an empty string.
# The words in the input String will only contain valid consecutive numbers.
#
# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""

# My solution

def order(sentence):
    new_sentence = []
    count = 1
    for x in range(0, len(sentence.split())):
        for word in sentence.split():
            if str(count) in word:
                new_sentence += [word]
                count += 1
    return ' '.join(new_sentence)

# solutions from cw

def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))


# -------

def extract_number(word):
    for l in word:
        if l.isdigit(): return int(l)
    return None

def order(sentence):
    return ' '.join(sorted(sentence.split(), key=extract_number))
# Write a function, which takes a non-negative integer (seconds) as input
# and returns the time in a human-readable format (HH:MM:SS)
#
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
#
# You can find some examples in the test fixtures.
#

# My solution

def make_readable(seconds):
    H = 0
    M = 0
    S = 0
    for sec in range(1,seconds+1):
            S += 1
            if S == 60:
                M += 1
                S = 0
                if M == 60:
                    H += 1
                    M = 0


    return "%02i:%02i:%02i" % (H, M, S)


print(make_readable(359999))

# CW solutions

def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

###

def make_readable(seconds):
    h= seconds/60**2
    m= (seconds%60**2)/60
    s= (seconds%60**2%60)
    return "%02d:%02d:%02d" % (h, m, s)
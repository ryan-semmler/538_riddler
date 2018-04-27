from math import ceil


"""
solves the Riddler Express at https://fivethirtyeight.com/features/how-fast-can-you-type-a-million-letters/
"""

def get_min_m(n):
    def inner(l):
        # l is a number of consecutive unoccupied spaces.
        # returns number of people who can fill those spaces.
        if l < 3:
            return 0
        return inner(int(l / 2)) + 1 + inner(ceil(l / 2) - 1)
    m = n * 2 - 1
    while True:
        res = 2 + inner(m - 2)
        if res >= n:
            return m
        m += 2 * (n - res) - 1

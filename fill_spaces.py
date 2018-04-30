from math import ceil


# solves the Riddler Express at
# https://fivethirtyeight.com/features/how-fast-can-you-type-a-million-letters/

def get_min_m(n):

    def gap(l):
        """
        gap takes as an argument a number of consecutive unoccupied spaces
        and returns the total number of people who can fit in those spaces.
        Assumes there are people on both sides of the gap.
        """
        if l < 3:
            return 0

        # places one person in the middle of the gap,
        # and starts over on the new smaller gaps on either side.
        return gap(int(l / 2)) + 1 + gap(ceil(l / 2) - 1)

    # start with m urinals for the minimum possible value of m for n people
    m = n * 2 - 1
    while True:
        # two people on the ends plus the number that can fit between them
        max_people = 2 + gap(m - 2)
        if max_people >= n:
            return m
        m += 2 * (n - max_people) - 1

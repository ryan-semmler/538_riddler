import random
import pdb


class House:
    def __init__(self):
        self.cash = 100

    def rob(self):
        other_house = houses[random.randint(0, 999)]
        while other_house is self:
            other_house = houses[random.randint(0, 999)]
        self.cash += other_house.cash
        other_house.cash = 0


index_totals = {i: 0 for i in range(1000)}
attempts = 200000
for _ in range(attempts):

    # creates identical starting House obj for each household
    houses = [House() for i in range(1000)]

    # PURGE
    for house in houses:
        house.rob()

    results = [house.cash for house in houses]
    for i in range(1000):
        index_totals[i] += results[i]

# analyze results
averages = [(i, index_totals[i] / attempts) for i in range(1000)]
ranked = sorted(averages, key=lambda tup: tup[1])[::-1]
for i in range(15):
    print(f"{i + 1}: position {ranked[i][0]}, averaging {ranked[i][1]}")
pdb.set_trace()

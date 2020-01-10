# https://fivethirtyeight.com/features/can-you-fool-the-bank-with-your-counterfeit-bills/

from math import ceil
from statistics import mean
import random


def get_ev(n, k=15000):
    """Returns expected value when adding n counterfeit bills to deposit"""
    def run_sim():
        real = 25
        fake = n
        orig_fake = n
        checks = ceil((25 + n) / 20)
        for _ in range(checks):
            check = random.randint(1, real + fake)
            if check > real:
                if random.randint(1, 4) == 1:
                    return 0
                fake -= 1
            else:
                real -= 1
        return 100 * (25 + orig_fake)

    results = [run_sim() for _ in range(k)]
    return mean(results)


ns = range(0, 251, 5)
results = {n: get_ev(n, 50000) for n in ns}
for n in results:
    print(f'EV({n}): {results[n]}')
print(f'\nmax: {max(results, key=lambda x: results[x])}')

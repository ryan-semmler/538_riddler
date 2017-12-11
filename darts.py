import random
from statistics import mean


# Finds answers for questions 2 and 3 of the Riddler Classic here:
# https://fivethirtyeight.com/features/how-quickly-can-you-throw-the-perfect-game-of-darts/

simulation_count = 10000000


def distance(self, other):
    a = abs(self[0] - other[0])
    b = abs(self[1] - other[1])
    return (a ** 2 + b ** 2) ** .5


def throw_dart():
    while True:
        x = random.random() * random.choice((-1, 1))
        y = random.random() * random.choice((-1, 1))
        if distance((x, y), (0, 0)) <= 1:
            return x, y


def game():
    throws = [throw_dart()]
    while True:
        throw = throw_dart()
        if min([distance(throw, other) for other in throws]) < 1:
            return len(throws)
        throws.append(throw)


simulation_results = [game() for _ in range(simulation_count)]
greater_than_one_prob = round(((simulation_count - simulation_results.count(1)) / simulation_count) * 100, 2)
expected_score = mean(simulation_results)
highest_score = max(simulation_results)
print(f"After {simulation_count} simulations:\n========================")
print(f"The probability of scoring more than one point is {greater_than_one_prob}%.")
print(f"The expected value of your score is {expected_score}")
print(f"The highest score was {highest_score}, which occurred {simulation_results.count(highest_score)} time(s)")

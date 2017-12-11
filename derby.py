import random


races = 100000
track_len = 200


class Horse:
    def __init__(self, number):
        self.prob = .5 + .02 * number
        self.number = number
        self.wins = 0

    def __repr__(self):
        return "Horse {}".format(self.number)

    def step(self):
        if self.prob > random.random():
            self.pos += 1
        else:
            self.pos -= 1


horses = [Horse(i) for i in range(1, 21)]


def race():
    for horse in horses:
        horse.pos = 0
    cont = True
    while cont:
        for horse in horses:
            horse.step()
            if horse.pos == track_len:
                horse.wins += 1
                cont = False


for _ in range(races):
    race()
res = {horse: horse.wins / races for horse in horses}
print(f"Results after {races} races:")
for horse in horses:
    print(f"{horse}: wins={horse.wins}")
print(f"ties: {sum([horse.wins for horse in horses]) - races}")

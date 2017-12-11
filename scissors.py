import random
import pdb


tries = 10000

beats = {
    'scissors': ['paper'],
    'paper'   : ['rock'],
    'rock'    : ['scissors', 'DS'],
    'DS'      : ['scissors', 'paper']
}

throws = [key for key in beats]


def game(w0, l0, throw):
    wins = w0
    losses = l0
    while max(wins, losses) < 2:
        if wins + losses != 0:
            won = round(own_throw='rock')
        else:
            won = round(throw)
        if won:
            wins += 1
        else:
            losses += 1
    return wins > losses


def round(own_throw=random.choice(throws)):
    other_throw = own_throw
    while other_throw == own_throw:
        other_throw = random.choice(throws)
    if own_throw == 'scissors' and other_throw == 'paper':
        return True
    return other_throw in beats[own_throw]


results1_1 = {throw: sum([round(throw) for _ in range(tries)]) / tries for throw in throws}
throw1_1 = max([key for key in results1_1], key=lambda thing: results1_1[thing])

results0_1 = {throw: sum([game(0, 1, throw) for i in range(tries)]) / tries for throw in throws}
throw0_1 = max([key for key in results0_1], key=lambda thing: results0_1[thing])

results1_0 = {throw: sum([game(1, 0, throw) for i in range(tries)]) / tries for throw in throws}
throw1_0 = max([key for key in results1_0], key=lambda thing: results1_0[thing])

results0_0 = {throw: sum([game(0, 0, throw) for i in range(tries)]) / tries for throw in throws}
throw0_0 = max([key for key in results0_0], key=lambda thing: results0_0[thing])

# results = {
#     '0-0': {
#       throw:
#     },
#     # '0-0': sum([game(0, 0) for _ in range(tries)]) / tries,
#     '0-1': sum([game(0, 1) for _ in range(tries)]) / tries,
#     '1-0': sum([game(1, 0) for _ in range(tries)]) / tries,
#     '1-1': {throw: sum([game(1, 1, throw) for _ in range(tries) for throw in throws]) / tries}
# }

pdb.set_trace()

import random
import pprint
from statistics import mean


# from https://fivethirtyeight.com/features/hark-two-holiday-puzzles/
player_count = 6
bills = 3
simulations = 100000


class Player:
    def __init__(self):
        self.bills = bills


def game():

    turns = 0
    players = [Player() for _ in range(6)]
    current_player = 0

    def turn(player_index):
        rolls = [random.randint(1, 6) for _ in range(3)]
        for roll in rolls:
            if players[player_index].bills > 0:
                if roll <= 2:
                    players[player_index - 1].bills += 1
                elif roll <= 4:
                    players[(player_index + 1) % player_count].bills += 1
                players[player_index].bills -= 1

    while len([player for player in players if player.bills > 0]) > 1:
        turn(current_player)
        current_player = (current_player + 1) % player_count
        turns += 1

    return turns


# show results
all_results = [game() for _ in range(simulations)]
print(f"Expected turns per game: {mean(all_results)}")

# shows number of turns, and how many games ended after that number of turns
results = {}
for result in all_results:
    if result not in results:
        results[result] = 1
    else:
        results[result] += 1
pprint.pprint(results)

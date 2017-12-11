import random
from pprint import pprint
from statistics import mean


sims = 25000

poss_spins = [round(.05 * i, 2) for i in range(1, 21)]


def spin():
    return random.choice(poss_spins)


def won(other_score):
    """
    Playing as third player in a three-player game
    """
    score = spin()
    if score > other_score:
        return True
    if score < other_score:
        score += spin()
    elif score == other_score:
        if score < .475:
            score += spin()
        else:
            return random.choice((True, False))
    if score > 1:
        return False

    return score > other_score


# show dict with p2's prob of beating p3 for each final score for p2. Assumes a three-player game
prob_of_beating_p3 = {score: 1 - mean([won(score) for _ in range(sims)]) for score in poss_spins}
pprint(prob_of_beating_p3)


def spin_again(first_spin):
    if first_spin == 1:
        return False
    chance_of_not_bust = 1 - first_spin
    possible_final_scores = [round(first_spin + .05 * i, 2) for i in range(1, round((1 - first_spin) / .05) + 1)]
    average_possible_score = mean([prob_of_beating_p3[score] for score in possible_final_scores])
    expected_win_prob_with_spin = average_possible_score * chance_of_not_bust
    print(first_spin, expected_win_prob_with_spin)
    return expected_win_prob_with_spin > prob_of_beating_p3[first_spin]

pprint({score: spin_again(score) for score in poss_spins})

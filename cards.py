import random


class Position:
    def __init__(self, pos):
        self.position = pos
        self.card = None

    def __repr__(self):
        return "Position {}: card={}".format(self.position, self.card.value if self.card else 'none')

    def is_filled(self):
        return self.card is not None

    def place(self, card):
        self.card = card


class Card:
    def __init__(self, order, value):
        self.order = order
        self.value = value

    def __repr__(self):
        return "Card {}, value={}".format(self.order, self.value)


def game():
    """
    format AB * CD, where A, B, C, and D are digits
    Optimal strategy: tens place always lower than ones place, and maximize difference b/w AB and CD
     SO: smallest digits in one number, largest digits in other number.
    """
    positions = [Position(i) for i in range(4)]

    deck = [i for i in range(10)]
    random.shuffle(deck)
    cards = [Card(i, deck[i]) for i in range(4)]
    cards_left = deck

    for card in cards:
        open_positions = [position for position in positions if not position.is_filled()]
        section = get_section(card.value, cards_left, 4 - card.order)
        open_positions[section].place(card)
        cards_left.remove(card.value)
    d = {
        'A': positions[0].card.value,
        'B': positions[1].card.value,
        'C': positions[2].card.value,
        'D': positions[3].card.value
    }
    return (10 * d['A'] + d['C']) *\
           (10 * d['B'] + d['D'])


def get_section(value, lst, divs):
    """
    divide sorted 'list' into 'divs' groups of equal length. return the group that 'value' would fit into
    """
    lst.sort()
    breakpoints = [lst[int(len(lst) / divs) * i - 1] for i in range(1, divs + 1)]
    for i in range(divs):
        if value <= breakpoints[i]:
            return i
    return divs - 1


tries = 1000000
print(sum([game() for _ in range(tries)]) / tries)

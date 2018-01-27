from pprint import pprint


"""
Solution to the puzzle at https://fivethirtyeight.com/features/how-often-does-the-senate-vote-in-palindromes/.
Finds all possible ways to divide an ostomachion into four groups of equal area without including neighboring
pieces in the same group.
"""


class Piece:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __add__(self, other):
        if type(other) == int:
            return other + self.size
        return self.size + other.size

    __radd__ = __add__

    # def __lt__(self, other):
    #     if type(other) == int:
    #         return self.size < other
    #     return self.size < other.size
    #
    # def __le__(self, other):
    #     if type(other) == int:
    #         return self.size <= other
    #     return self.size <= other.size
    #
    # def __gt__(self, other):
    #     if type(other) == int:
    #         return self.size > other
    #     return self.size > other.size
    #
    # def __ge__(self, other):
    #     if type(other) == int:
    #         return self.size >= other
    #     return self.size >= other.size
    #
    # def __str__(self):
    #     return "Piece " + self.name

    def __repr__(self):
        return "Piece " + self.name


class Group:
    def __init__(self, *pieces):
        self.pieces = list(pieces)

    def __contains__(self, item):
        return any([thing is item for thing in self.pieces])

    def __iter__(self):
        for item in self.pieces:
            yield item

    # def __eq__(self, other):
    #     if type(other) != type(self):
    #         return False
    #     return sorted([piece.name for piece in self.pieces]) == sorted([piece.name for piece in other.pieces])

    # def __len__(self):
    #     return len(self.pieces)

    def __repr__(self):
        return f"Group: {self.pieces}"

    def append(self, other):
        if other not in self.pieces:
            self.pieces.append(other)


names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
sizes = [12, 12, 6, 12, 24, 12, 3, 21, 3, 6, 6, 9, 6, 12]
pieces = [Piece(names[i], sizes[i]) for i in range(14)]
a, b, c, d, e, f, g, h, i, j, k, l, m, n = pieces
neighbors = {
    a: [b, f],
    b: [a, f, c],
    c: [b, h, d],
    d: [c, j, k, e],
    e: [d, g],
    f: [a, b, h, i, m],
    g: [e, l],
    h: [i, f, c, j],
    i: [m, f, h],
    j: [h, d, n],
    k: [n, d, l],
    l: [g, k],
    m: [f, i],
    n: [j, k]
    }


def use_different_pieces(*groups):
    pieces = [piece for group in groups for piece in group.pieces]
    for piece in pieces:
        if pieces.count(piece) > 1:
            return False
    return True


def has_no_neighbors(pieces_list):
    for piece in pieces_list:
        for neighbor in neighbors[piece]:
            if neighbor in pieces_list:
                return False
    return True


def get_groups(pieces):
    groups = []
    for u in range(len(pieces)):
        a = pieces[u]
        if u < (len(pieces) - 1):
            for v in range(u + 1, len(pieces)):
                b = pieces[v]
                if sum((a, b)) == 36:
                    groups.append([a, b])
                if sum((a, b)) < 36 and v < (len(pieces) - 1):
                    for w in range(v + 1, len(pieces)):
                        c = pieces[w]
                        if sum((a, b, c)) == 36:
                            groups.append([a, b, c])
                        if sum((a, b, c)) < 36 and w < (len(pieces) - 1):
                            for x in range(w + 1, len(pieces)):
                                d = pieces[x]
                                if sum((a, b, c, d)) == 36:
                                    groups.append([a, b, c, d])
                                if sum((a, b, c, d)) < 36 and x < (len(pieces) - 1):
                                    for y in range(x + 1, len(pieces)):
                                        e = pieces[y]
                                        if sum((a, b, c, d, e)) == 36:
                                            groups.append([a, b, c, d, e])
                                        if sum((a, b, c, d, e)) < 36 and y < (len(pieces) - 1):
                                            for z in range(y + 1, len(pieces)):
                                                f = pieces[z]
                                                if sum((a, b, c, d, e, f)) == 36:
                                                    groups.append([a, b, c, d, e, f])
    return [Group(*group) for group in groups if has_no_neighbors(group)]


def get_solutions(groups):
    solutions = []
    for w in range(len(groups) - 3):
        for x in range(w + 1, len(groups) - 2):
            for y in range(x + 1, len(groups) - 1):
                for z in range(y + 1, len(groups)):
                    if use_different_pieces(groups[w], groups[x], groups[y], groups[z]):
                        solutions.append([groups[w], groups[x], groups[y], groups[z]])
    return solutions


def main():
    groups = get_groups(pieces)
    solutions = get_solutions(groups)
    print(f"{len(solutions)} solutions:\n------------------------")
    pprint(solutions)


main()

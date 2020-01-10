import requests

request = requests.get('https://norvig.com/ngrams/enable1.txt')
words = sorted(request.text.split('\r\n'), key=len, reverse=True)

tile_quants = [13, 3, 3, 6, 18, 3, 4, 3, 12, 2, 2, 5, 3, 8, 11, 3, 2, 9, 6, 9, 6, 3, 3, 2, 3, 2]
tiles = dict(zip('abcdefghijklmnopqrstuvwxyz', tile_quants))
# tiles gives the quantity remaining for each letter

import pdb; pdb.set_trace()

class Board:
    def __init__(self, tiles, board=None):
        self.tiles = tiles  # could be figured out from board, but given to save time
        if board:
            self.board = board
        else:
            self.board = [[' ' for _ in range(300)] for _ in range(300)]

    def count_words(self):
        # get horizontal words
        h_words = sum(len(word) > 1 for row in self.board for word in ''.join(row).split())

        # get vertical words
        v_words = 0
        for i in range(len(self.board[0])):
            col = [self.board[j][i] for j in range(len(self.board))]
            v_words += sum(len(word) > 1 for word in ''.join(col).split())

        return h_words + v_words

    def can_place(self, word):
        """return bool, whether word can be placed on board"""

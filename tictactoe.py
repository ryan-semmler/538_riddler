class GameBoard:
    """Represents a tic-tac-toe board in a specific state. Later moves will be new GameBoard objects."""
    def __init__(self, size=3, board=None):

        # board is the game board, represented as a list. Defaults to a new, empty game board.
        if board:
            self.board = board
        else:
            self.board = []
            for _ in range(size):
                self.board.append([None] * size)

        # size is the number of spaces on each side of the board. Defaults to a 3x3 game board.
        self.size = size

        # spaces is a list of the empty spaces on the game board, as tuples
        self.spaces = [(y, x) for y in range(self.size) for x in range(self.size) if not self.board[y][x]]

        # Determines whether it's X's or O's turn
        self.mark = ('X', 'O')[(size ** 2 - len(self.spaces)) % 2]

        self.winners = (['X'] * size, ['O'] * size)

    def __repr__(self):
        return self.mark + "'s turn\n" + '\n'.join(map(str, self.board))

    def game_over(self):
        """Returns True if one player has won, otherwise False"""
        for row in self.board:  # check for winning rows
            if row in self.winners:
                return True
        for col in range(self.size):  # check for winning columns
            if [self.board[i][col] for i in range(self.size)] in self.winners:
                return True
        if [self.board[i][i] for i in range(self.size)] in self.winners:  # check first diagonal
            return True
        return [self.board[self.size - 1 - i][i] for i in range(self.size)] in self.winners  # check other diagonal

    def move(self, space):
        """Returns a new game board, as a list, representing the board after a move to a given space"""
        new_board = [[item for item in sub_l] for sub_l in self.board]
        new_board[space[0]][space[1]] = self.mark
        return new_board


def get_possible_games(board):
    """Determines the number of games possible from a given starting position. board is a GameBoard object."""

    # checks whether the game is over, only if enough turns have elapsed for a game over to be possible
    if len(board.spaces) <= (board.size - 1) ** 2 and board.game_over():
        return 1

    # There are always exactly two possible games from a board with only two blank spaces.
    if len(board.spaces) == 2:
        return 2

    # recursively call get_possible_games for each possible move this turn
    return sum(get_possible_games(GameBoard(size=board.size, board=board.move(space))) for space in board.spaces)


print("Possible games of tic-tac-toe: {}".format(get_possible_games(GameBoard())))
import pdb; pdb.set_trace()

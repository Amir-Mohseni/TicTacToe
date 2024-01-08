import copy

from Board import *


class AI:
    def __init__(self, name):
        self.name = name

    def makeMove(self, board, depth=0):
        if depth % 2 == 0:
            best_answer = -2, -1, -1
        else:
            best_answer = 2, -1, -1
        for i in range(3):
            for j in range(3):
                if board.board[i][j] == "-":
                    new_board = Board()
                    new_board.board = copy.deepcopy(board.board)
                    new_board.placePiece(i, j)
                    if new_board.checkFinished():
                        if new_board.winner is None:
                            return 0, i, j
                        else:
                            return 1, i, j
                    else:
                        if depth % 2 == 0:
                            best_answer = max(best_answer, self.makeMove(new_board, depth + 1))
                        else:
                            best_answer = min(best_answer, self.makeMove(new_board, depth + 1))
        return best_answer


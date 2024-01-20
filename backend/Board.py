class Board:
    pieces_dict = {0: 'X', 1: 'O'}
    players_dict = {'X': 0, 'O': 1}

    def __init__(self):
        self.board = [['-' for x in range(3)] for y in range(3)]
        self.gameFinished = False
        self.winner = None
        self.turn = 0

    def checkFinished(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2] and self.board[i][0] != '-':
                self.winner = self.board[i][0]
                self.gameFinished = True
                return True
            if self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i] and self.board[0][i] != '-':
                self.winner = self.board[0][i]
                self.gameFinished = True
                return True

        if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2] and self.board[0][0] != '-':
            self.winner = self.board[0][0]
            self.gameFinished = True
            return True
        if self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0] and self.board[0][2] != '-':
            self.winner = self.board[0][2]
            self.gameFinished = True
            return True

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-':
                    self.gameFinished = False
                    self.winner = None
                    return False

        self.gameFinished = True
        return True

    def placePiece(self, x, y):
        if x < 0 or x > 2 or y < 0 or y > 2:
            return "Invalid Move"
        if self.board[x][y] == '-':
            self.board[x][y] = Board.pieces_dict[self.turn]
            self.turn = (self.turn + 1) % 2
            return "Piece Placed"
        else:
            return "Invalid Move"

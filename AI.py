class AI:
    def __init__(self, name):
        self.name = name

    def minimax(self, board, func, ai_piece, human_piece):
        if board.checkFinished():
            if board.winner is None:
                return 0, -1, -1
            elif board.winner == ai_piece:
                return 1, -1, -1
            else:
                return -1, -1, -1

        if func == "max":
            best_score = -2
            best_x = -1
            best_y = -1
            for i in range(3):
                for j in range(3):
                    if board.board[i][j] == "-":
                        board.board[i][j] = ai_piece
                        score, x, y = self.minimax(board, "min", ai_piece, human_piece)
                        board.board[i][j] = "-"
                        if score > best_score:
                            best_score = score
                            best_x = i
                            best_y = j
            return best_score, best_x, best_y
        else:
            best_score = 2
            best_x = -1
            best_y = -1
            for i in range(3):
                for j in range(3):
                    if board.board[i][j] == "-":
                        board.board[i][j] = human_piece
                        score, x, y = self.minimax(board, "max", ai_piece, human_piece)
                        board.board[i][j] = "-"
                        if score < best_score:
                            best_score = score
                            best_x = i
                            best_y = j
            return best_score, best_x, best_y

    def makeMove(self, board, pieces):
        ai_piece = pieces[0]
        human_piece = pieces[1]
        for i in range(3):
            for j in range(3):
                if board.board[i][j] == "-":
                    board.board[i][j] = human_piece
                    if board.checkFinished():
                        board.board[i][j] = "-"
                        return 0, i, j
                    board.board[i][j] = "-"
        return self.minimax(board, "max", ai_piece, human_piece)

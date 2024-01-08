import os
from time import sleep

from Board import *
from AI import *
from Player import *


def emptyScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]

    def display(self):
        for i in range(3):
            for j in range(3):
                print(self.board.board[i][j], end=" ")
            print()

    def play(self):
        while not self.board.gameFinished:
            sleep(0.8)
            emptyScreen()
            print(self.players[self.board.turn].name + "'s turn")
            self.display()

            if isinstance(self.players[self.board.turn], Player):
                x = int(input("Enter x: "))
                y = int(input("Enter y: "))

                print(self.board.placePiece(x, y))
            else:
                best_move = self.players[self.board.turn].makeMove(self.board)
                self.board.placePiece(best_move[1], best_move[2])
                print("Computer placed piece at " + str(best_move[1]) + ", " + str(best_move[2]))
            self.board.checkFinished()
        sleep(0.8)

        emptyScreen()
        self.display()

        if self.board.winner is None:
            print("Tie")
        else:
            print(self.players[Board.players_dict[self.board.winner]].name + " wins!")

        input("Press Enter to continue...")
        return


if __name__ == "__main__":
    p1, p2 = None, None
    while True:
        game_type = input("Single Player or Multiplayer? (1/2): ")
        if game_type == "1":
            while True:
                turn = input("Do you want to be X or O? (X/O): ")
                if turn == "X":
                    p1 = Player(input("Enter Player's name: "))
                    p2 = AI("Computer")
                    break
                elif turn == "O":
                    p1 = AI("Computer")
                    p2 = Player(input("Enter Player's name: "))
                    break
                else:
                    print("Invalid Input")
                    continue
            break
        elif game_type == "2":
            p1 = Player(input("Enter Player 1's name: "))
            p2 = Player(input("Enter Player 2's name: "))
            break
        else:
            print("Invalid Input")
            continue

    g = Game(p1, p2)
    g.play()

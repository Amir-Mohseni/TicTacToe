import os
from time import sleep

from Board import *
from Player import *


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]

    def emptyScreen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display(self):
        for i in range(3):
            for j in range(3):
                print(self.board.board[i][j], end=" ")
            print()

    def play(self):
        while not self.board.gameFinished:
            sleep(0.8)
            self.emptyScreen()
            print(self.players[self.board.turn].name + "'s turn")
            self.display()

            x = int(input("Enter x: "))
            y = int(input("Enter y: "))

            print(self.board.placePiece(x, y))

            self.board.checkFinished()
        sleep(0.8)

        self.emptyScreen()
        self.display()

        if self.board.winner is None:
            print("Tie")
        else:
            print(self.board.winner + " wins!")

        input("Press Enter to continue...")
        return


if __name__ == "__main__":
    p1 = Player("Player 1")
    p2 = Player("Player 2")
    g = Game(p1, p2)
    g.play()

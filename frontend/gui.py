import pygame
import sys
from backend.Board import Board

def main():
    # Initialize pygame
    pygame.init()

    # Set up the window
    windowSurface = pygame.display.set_mode((600, 500), 0, 32)
    pygame.display.set_caption('Tic Tac Toe')

    # Set up the colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Set up fonts
    basicFont = pygame.font.SysFont(None, 48)

    # display 3 by 3 grid with pygame
    def display(board):
        for i in range(3):
            for j in range(3):
                text = basicFont.render(board.board[i][j], True, BLACK, WHITE)
                textRect = text.get_rect()
                textRect.centerx = 150 + 100 * i
                textRect.centery = 150 + 100 * j
                windowSurface.blit(text, textRect)

    #update the board with the player's move
    def updateBoard(board, x, y):
        if board.board[x][y] == '-':
            board.board[x][y] = Board.pieces_dict[board.turn]
            board.turn = (board.turn + 1) % 2
            return "Piece Placed"
        else:
            return "Invalid Move"

    # Run the game loop
    while True:
        # Set up the background
        windowSurface.fill(WHITE)
        # Draw the board
        pygame.draw.line(windowSurface, BLACK, (200, 100), (200, 400), 5)
        pygame.draw.line(windowSurface, BLACK, (300, 100), (300, 400), 5)
        pygame.draw.line(windowSurface, BLACK, (100, 200), (400, 200), 5)
        pygame.draw.line(windowSurface, BLACK, (100, 300), (400, 300), 5)
        # Draw the Xs and Os
        board = Board()
        display(board)
        # Get the player's move
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    x = int((x - 150) / 100)
                    y = int((y - 150) / 100)
                    print(x, y)
                    print(updateBoard(board, x, y))
                    display(board)
                    if board.checkFinished():
                        if board.winner is None:
                            print("Tie")
                        else:
                            print(Board.players_dict[board.winner] + " wins!")
                        input("Press Enter to continue...")
                        sys.exit()
                    break
            pygame.display.update()

if __name__ == "__main__":
    main()
from time import sleep

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

    # update the board with the player's move
    def updateBoard(board, x, y):
        if board.board[x][y] == '-':
            board.board[x][y] = Board.pieces_dict[board.turn]
            board.turn = (board.turn + 1) % 2
            return "Piece Placed"
        else:
            return "Invalid Move"

    # Function to display winner announcement window
    def display_winner_announcement(text):
        winner_width, winner_height = 300, 150
        winner_screen = pygame.display.set_mode((winner_width, winner_height))
        pygame.display.set_caption("Session Ended")

        font = pygame.font.Font(None, 16)
        winner_text = font.render(text, True, (0, 0, 0))
        text_rect = winner_text.get_rect(center=(winner_width // 2, winner_height // 2))

        ok_button_rect = pygame.Rect(winner_width // 2 - 50, winner_height - 50, 100, 30)
        ok_button_color = (0, 128, 255)
        ok_button_text = font.render("Replay?", True, (0, 0, 0))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if ok_button_rect.collidepoint(event.pos):
                        # Exit the function when the "OK" button is clicked
                        pygame.quit()
                        main()

            winner_screen.fill((255, 255, 255))
            pygame.draw.rect(winner_screen, ok_button_color, ok_button_rect)
            winner_screen.blit(winner_text, text_rect)
            winner_screen.blit(ok_button_text, ok_button_rect)

            pygame.display.flip()

    def game_loop():
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
                        print(x, y)
                        x = int((x - 101) / 100)
                        y = int((y - 101) / 100)
                        print(x, y)
                        print(updateBoard(board, x, y))
                        display(board)

                        announcement_text = str()

                        if board.checkFinished():
                            if board.winner is None:
                                announcement_text = ("Tie")
                            else:
                                announcement_text = str(board.winner) + " wins!"
                            pygame.display.update()
                            display_winner_announcement(announcement_text)
                            sleep(2)
                            return
                        break
                pygame.display.update()

    game_loop()
    pygame.quit()


if __name__ == "__main__":
    main()

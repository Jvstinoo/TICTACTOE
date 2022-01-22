import time
import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()

'''TIC TAC TOE'''
BLACK = (0, 0, 0)
WHITE = (255, 0, 0)
RAND = (33, 49, 29)
WIDTH, HEIGHT = 600, 600
CLOCK = pygame.time.Clock()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
click = False
squares = [None] * 9
sq1 = pygame.Rect(20, 20, 20, 20)
'''Pygame mouse detection'''
score_font = pygame.font.SysFont('comicsans', 45)
squareNet = [pygame.Rect(60, 20, 160, 160), pygame.Rect(220, 20, 160, 160), pygame.Rect(380, 20, 160, 160), pygame.Rect(60, 180, 160, 160), pygame.Rect(
    220, 180, 160, 160), pygame.Rect(380, 180, 160, 160), pygame.Rect(60, 340, 160, 160), pygame.Rect(220, 340, 160, 160), pygame.Rect(380, 340, 160, 160)]
gameBoard = {0: ' ', 1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' '}
x_score = 0
o_score = 0


def emptyGameBoard():
    for i in gameBoard:
        gameBoard[i] = ' '


def drawSquares():
    for i in squareNet:
        pygame.draw.rect(WIN, RAND, i, 2)


def drawX():
    for key, val in gameBoard.items():
        if val == 'X':
            pygame.draw.line(WIN, WHITE, (squareNet[key].x + 5, squareNet[key].y + 5),
                             (squareNet[key].x + 155, squareNet[key].y + 155), 6)
            pygame.draw.line(
                WIN, WHITE, (squareNet[key].x + 155, squareNet[key].y+5), (squareNet[key].x+5, squareNet[key].y+155), 6)


def checkWin():
    global x_score, o_score
    for horizontal in range(0, len(gameBoard), 3):
        trial = list(gameBoard.values())[horizontal:horizontal+3]
        if trial.count('X') == 3 or trial.count('O') == 3:
            if trial[0] == 'X':
                x_score += 1
                time.sleep(.1)
                emptyGameBoard()
            else:
                print('YOU LOSE')

    for vertical in range(0, 3):
        vals = list(gameBoard.values())
        trial = [vals[vertical], vals[vertical+3], vals[vertical+6]]
        if trial.count('X') == 3 or trial.count('O') == 3:
            if trial[0] == 'X':
                x_score += 1
                time.sleep(.1)
                emptyGameBoard()
            else:
                print('YOU LOSE')

    diagonal = [gameBoard[0], gameBoard[4], gameBoard[8]]
    if diagonal.count('X') == 3 or diagonal.count('O') == 3:
        if diagonal[0] == 'X':
            x_score += 1
            time.sleep(.1)
            emptyGameBoard()
        else:
            print('YOU LOSE')

    reverse_diagonal = [gameBoard[2], gameBoard[4], gameBoard[6]]
    if reverse_diagonal.count('X') == 3 or reverse_diagonal.count('O') == 3:
        if reverse_diagonal[0] == 'X':
            x_score += 1
            time.sleep(.1)
            emptyGameBoard()
        else:
            print('YOU LOSE')


def drawScore():
    x_score_render = score_font.render(f'X: {x_score}', False, WHITE)
    o_score_render = score_font.render(f'O: {o_score}', False, WHITE)
    WIN.blit(x_score_render, (WIDTH//2-80, HEIGHT - 60))
    WIN.blit(o_score_render, (WIDTH//2+20, HEIGHT - 60))


running = True
while running:
    WIN.fill(BLACK)

    mx, my = pygame.mouse.get_pos()
    for j in range(len(squareNet)):
        if squareNet[j].collidepoint((mx, my)) and pygame.mouse.get_pressed()[0]:
            if gameBoard[j] == ' ':
                gameBoard[j] = 'X'
    drawSquares()
    drawScore()
    checkWin()
    drawX()

    # mouseDetection()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    CLOCK.tick(60)
    pygame.display.update()

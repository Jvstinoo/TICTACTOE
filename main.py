import time
import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()

'''TIC TAC TOE'''
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (54, 130, 189)
SCORE_BLUE = (30, 69, 136)
PURPLE = (164, 31, 102)
RAND = (33, 49, 29)
WIDTH, HEIGHT = 600, 600
CLOCK = pygame.time.Clock()
pygame.display.set_caption("TIC TAC TOE")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
'''Pygame mouse detection'''
score_font = pygame.font.SysFont('comicsans', 45)
x_o_font = pygame.font.Font('PressStart2P-Regular.ttf', 140)
squareNet = [pygame.Rect(60, 20, 160, 160), pygame.Rect(220, 20, 160, 160), pygame.Rect(380, 20, 160, 160), pygame.Rect(60, 180, 160, 160), pygame.Rect(
    220, 180, 160, 160), pygame.Rect(380, 180, 160, 160), pygame.Rect(60, 340, 160, 160), pygame.Rect(220, 340, 160, 160), pygame.Rect(380, 340, 160, 160)]
gameBoard = {0: ' ', 1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' '}
x_score = 0
o_score = 0
x_turn = 0
o_turn = 0


def emptyGameBoard():
    for i in gameBoard:
        gameBoard[i] = ' '


def drawSquares():
    for i in squareNet:
        pygame.draw.rect(WIN, WHITE, i, 4)


def drawX():
    x_render = x_o_font.render('X', False, BLUE)

    for key, val in gameBoard.items():
        if val == 'X':
            WIN.blit(x_render, (squareNet[key].x+20, squareNet[key].y+17))
            '''pygame.draw.line(WIN, WHITE, (squareNet[key].x + 5, squareNet[key].y + 5),
                             (squareNet[key].x + 155, squareNet[key].y + 155), 6)
            pygame.draw.line(
                WIN, WHITE, (squareNet[key].x + 155, squareNet[key].y+5), (squareNet[key].x+5, squareNet[key].y+155), 6)
'''


def itsDraw():
    global x_turn, o_turn
    if ' ' not in list(gameBoard.values()):
        emptyGameBoard()
        x_turn = 0
        o_turn = 0


def drawO():
    o_render = x_o_font.render('O', False, PURPLE)
    for key, val in gameBoard.items():
        if val == 'O':
            WIN.blit(o_render, (squareNet[key].x+20, squareNet[key].y+17))
            '''pygame.draw.circle(
                WIN, WHITE, (squareNet[key].x+80, squareNet[key].y+80), 80, 6)'''


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
                o_score += 1
                time.sleep(.1)
                emptyGameBoard()

    for vertical in range(0, 3):
        vals = list(gameBoard.values())
        trial = [vals[vertical], vals[vertical+3], vals[vertical+6]]
        if trial.count('X') == 3 or trial.count('O') == 3:
            if trial[0] == 'X':
                x_score += 1
                start_pos = (squareNet[vertical].x, squareNet[vertical].y)
                end_pos = (squareNet[vertical+6].x, squareNet[vertical+6].y)
                pygame.draw.line(WIN, WHITE, start_pos, end_pos, 2)
                emptyGameBoard()
            else:
                o_score += 1
                time.sleep(.1)
                emptyGameBoard()

    diagonal = [gameBoard[0], gameBoard[4], gameBoard[8]]
    if diagonal.count('X') == 3 or diagonal.count('O') == 3:
        if diagonal[0] == 'X':
            pygame.draw.line(
                WIN, WHITE, (squareNet[0].x, squareNet[0].y), (squareNet[8].x+160, squareNet[8].y+160), 4)
            x_score += 1
            pygame.time.delay(100)
            emptyGameBoard()
        else:
            o_score += 1
            time.sleep(.1)
            emptyGameBoard()

    reverse_diagonal = [gameBoard[2], gameBoard[4], gameBoard[6]]
    if reverse_diagonal.count('X') == 3 or reverse_diagonal.count('O') == 3:
        if reverse_diagonal[0] == 'X':
            x_score += 1
            pygame.draw.line(
                WIN, WHITE, (squareNet[2].x+160, squareNet[2].y), (squareNet[6].x, squareNet[6].y+160), 2)
            time.sleep(2)
            emptyGameBoard()
        else:
            o_score += 1
            time.sleep(.1)
            emptyGameBoard()


def AI():
    global x_turn, o_turn
    if x_turn-o_turn == 1:
        for key, val in gameBoard.items():
            if val == ' ':
                gameBoard[key] = 'O'
                o_turn += 1
                break


def getXCount(dic):
    return list(dic.values()).count('X')


def getOCount(dic):
    return list(dic.values()).count('O')


def chosenSpot(dic):
    vals = list(dic.values())
    keys = list(dic.keys())
    return keys[vals.index(' ')]


def horizontalCheck():
    global x_turn, o_turn
    for i in range(0, len(gameBoard), 3):
        hor = {i: gameBoard[i], i+1: gameBoard[i+1], i+2: gameBoard[i+2]}
        if getXCount(hor) > 1 and getOCount(hor) < 1 and (x_turn-o_turn == 1):
            gameBoard[chosenSpot(hor)] = 'O'
            o_turn += 1


def verticalCheck():
    global x_turn, o_turn
    for i in range(0, 3):
        vert = {i: gameBoard[i], i+3: gameBoard[i+3], i+6: gameBoard[i+6]}
        if getXCount(vert) > 1 and getOCount(vert) < 1 and (x_turn-o_turn == 1):
            gameBoard[chosenSpot(vert)] = 'O'
            o_turn += 1


def diagonalCheck():
    global x_turn, o_turn
    diag = {0: gameBoard[0], 4: gameBoard[4], 8: gameBoard[8]}
    if getXCount(diag) > 1 and getOCount(diag) < 1 and (x_turn-o_turn == 1):
        gameBoard[chosenSpot(diag)] = 'O'
        o_turn += 1


def reverseDiagonalCheck():
    global x_turn, o_turn
    rev_diag = {2: gameBoard[2], 4: gameBoard[4], 6: gameBoard[6]}
    if getXCount(rev_diag) > 1 and getOCount(rev_diag) < 1 and (x_turn-o_turn == 1):
        gameBoard[chosenSpot(rev_diag)] = 'O'
        o_turn += 1


def drawScore():
    x_score_render = score_font.render(f'X: {x_score}', False, BLUE)
    o_score_render = score_font.render(f'O: {o_score}', False, PURPLE)
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
                x_turn += 1
    checkWin()
    itsDraw()
    drawSquares()
    drawScore()
    horizontalCheck()
    verticalCheck()
    diagonalCheck()
    reverseDiagonalCheck()
    AI()

    drawX()
    drawO()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    CLOCK.tick(60)
    pygame.display.update()

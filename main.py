import pygame
import time

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
current_time = 0
event_timer = 0
x_o_font = pygame.font.Font('PressStart2P-Regular.ttf', 140)
squareNet = [pygame.Rect(60, 20, 160, 160), pygame.Rect(220, 20, 160, 160), pygame.Rect(380, 20, 160, 160), pygame.Rect(60, 180, 160, 160), pygame.Rect(
    220, 180, 160, 160), pygame.Rect(380, 180, 160, 160), pygame.Rect(60, 340, 160, 160), pygame.Rect(220, 340, 160, 160), pygame.Rect(380, 340, 160, 160)]
gameBoard = {0: ' ', 1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' '}
x_score = 0
o_score = 0
x_turn = 0
o_turn = 0
won = False


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
    if ' ' not in list(gameBoard.values()) and not won:
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
    global x_score, o_score, event_timer, current_time, flag_win, won

    for horizontal in range(0, len(gameBoard), 3):
        trial = list(gameBoard.values())[horizontal:horizontal+3]
        if trial.count('X') == 3 or trial.count('O') == 3:

            won = True
            return squareNet[horizontal], squareNet[horizontal+3], squareNet[horizontal], 'Horizontal'

    for vertical in range(0, 3):
        vals = list(gameBoard.values())
        trial = [vals[vertical], vals[vertical+3], vals[vertical+6]]
        if trial.count('X') == 3 or trial.count('O') == 3:
            won = True
            return squareNet[vertical], squareNet[vertical+6], squareNet[vertical], 'Vertical'

    diagonal = [gameBoard[0], gameBoard[4], gameBoard[8]]
    if diagonal.count('X') == 3 or diagonal.count('O') == 3:
        won = True
        return squareNet[0], squareNet[8], diagonal[0], 'Diagonal'

    reverse_diagonal = [gameBoard[2], gameBoard[4], gameBoard[6]]
    if reverse_diagonal.count('X') == 3 or reverse_diagonal.count('O') == 3:
        won = True
        return squareNet[2], squareNet[6], gameBoard[2], 'Rev_Diagonal'


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
        if getXCount(hor) > 1 and getOCount(hor) < 1 and (x_turn-o_turn == 1) and not won:
            gameBoard[chosenSpot(hor)] = 'O'
            o_turn += 1


def verticalCheck():
    global x_turn, o_turn
    for i in range(0, 3):
        vert = {i: gameBoard[i], i+3: gameBoard[i+3], i+6: gameBoard[i+6]}
        if getXCount(vert) > 1 and getOCount(vert) < 1 and (x_turn-o_turn == 1) and not won:
            gameBoard[chosenSpot(vert)] = 'O'
            o_turn += 1


def diagonalCheck():
    global x_turn, o_turn
    diag = {0: gameBoard[0], 4: gameBoard[4], 8: gameBoard[8]}
    if getXCount(diag) > 1 and getOCount(diag) < 1 and (x_turn-o_turn == 1) and not won:
        gameBoard[chosenSpot(diag)] = 'O'
        o_turn += 1


def reverseDiagonalCheck():
    global x_turn, o_turn
    rev_diag = {2: gameBoard[2], 4: gameBoard[4], 6: gameBoard[6]}
    if getXCount(rev_diag) > 1 and getOCount(rev_diag) < 1 and (x_turn-o_turn == 1) and not won:
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
    winning_side = ''
    if won:
        win_details = checkWin()
        winning_side = checkWin()[2]
        if win_details[-1] == 'Diagonal':
            pygame.draw.line(
                WIN, WHITE, (win_details[0].x, win_details[0].y), (win_details[1].x+160, win_details[1].y+160), 8)
        if win_details[-1] == 'Vertical':
            pygame.draw.line(
                WIN, WHITE, (win_details[0].x + 80, win_details[0].y), (win_details[1].x+80, win_details[1].y+160), 4)

        if win_details[-1] == 'Rev_Diagonal':
            pygame.draw.line(
                WIN, WHITE, (win_details[0].x+160, win_details[0].y), (win_details[1].x, win_details[1].y+160), 4)

        if win_details[-1] == 'Horizontal':
            pygame.draw.line(
                WIN, WHITE, (win_details[0].x, win_details[0].y+80), (win_details[1].x+160, win_details[1].y+80), 4)
        event_timer = pygame.time.get_ticks()
        won = False
    # current_time = pygame.time.get_ticks()
    if event_timer > 6000:
        emptyGameBoard()
        if winning_side == 'X':
            x_score += 1
        else:
            o_score += 1
        event_timer = 0

    print(current_time, event_timer)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    CLOCK.tick(60)
    pygame.display.update()


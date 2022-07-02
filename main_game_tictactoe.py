"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

TIC TAC TOE GAME

author: Lucia Solčanová
email: lucia.solcanova@gmail.com
discord: Lucka #0676
"""

import os

from art_tictactoe import art


# ------------- Úvodní text ------------- 
    # pozdravení uživatele
    # vypsání pravidel hry



player_x = 'X'      # tento hráč začíná vždy první
player_o = 'O'
expectation = 0
separator = '========================================'
separator_2 = '--------------------------------------------'

def great():
    '''Tato funkce pozdraví uživatele a vypíše pravidla hry'''

    print(art)
    print('Welcome to Tic Tac Toe')
    print(separator)
    print('''GAME RULES:\nEachEach player can place one mark (or stone)
    per turn on the 3x3 grid. The WINNER is
    who succeeds in placing three of their
    marks in a:\n
    * horizontal,
    * vertical or
    * diagonal row''')
    print(separator)
    print("Let's start the game")
    print(separator_2)

great()

# Vytvoření hrací plochy

board = [' ',' ',' ',
         ' ',' ',' ',
         ' ',' ',' ']

def playing_board(board):
    '''Nakreslení hrací plochy'''

    print('+---+---+---+')
    print(f'| {board[0]} | {board[1]} | {board[2]} |')
    print('+---+---+---+')
    print(f'| {board[3]} | {board[4]} | {board[5]} |')
    print('+---+---+---+')
    print(f'| {board[6]} | {board[7]} | {board[8]} |')
    print('+---+---+---+')

playing_board(board)

def check(moves):
    '''Pokud index není prázdný, upozorní uživatele pro zadání jiného čísla'''

    if board[moves - 1] != ' ':
        print('Try a different number!')


# Kontrola vítěze

def winner():
    return    ((board[0] != ' ' and board[0] == board[4] == board[8])
            or (board[2] != ' ' and board[2] == board[4] == board[6])
            or (board[0] != ' ' and board[0] == board[1] == board[2])
            or (board[3] != ' ' and board[3] == board[4] == board[5])
            or (board[6] != ' ' and board[6] == board[7] == board[8])
            or (board[0] != ' ' and board[0] == board[3] == board[6])
            or (board[1] != ' ' and board[1] == board[4] == board[7])
            or (board[2] != ' ' and board[2] == board[5] == board[8]))

# Výhra X, O nebo remíza

for expectation in range(9):
    if expectation % 2 == 0:
        print(separator)
        moves = int(input(f'Player {player_x} | Please enter your move number: '))
        print(separator)
        check(moves)
        board[moves -1] = player_x
        playing_board(board)
        win = winner()
        if win is True:
            print(separator)
            print(f'Congratulations, the player {player_x} WON!')
            print(separator)
            break
        elif expectation == 8:
            print(separator)
            print("It's a draw!")
            print(separator)

    else:
        print(separator)
        moves = int(input(f'Player {player_o} | Please enter your move number: '))
        print(separator)
        check(moves)
        board[moves -1] = player_o
        playing_board(board)
        win = winner()
        if win is True:
            print(separator)
            print(f'Congratulations, the player {player_o} WON!')
            print(separator)
            break
        elif expectation == 8:
            print(separator)
            print("It's a draw!")
            print(separator)






















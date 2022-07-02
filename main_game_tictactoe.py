"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

TIC TAC TOE GAME

author: Lucia Solčanová
email: lucia.solcanova@gmail.com
discord: Lucka #0676
"""

import os
import random

from art_tictactoe import art


# ------------- Úvodní text ------------- 
    # pozdravení uživatele
    # vypsání pravidel hry

def great():
    '''Tato funkce pozdraví uživatele a vypíše pravidla hry'''

    print(art)

    separator = '========================================'
    separator_2 = '--------------------------------------------'

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

# Výzva hráči, aby umístil kámen na pozici

def player(board):
    '''Funkce předpokládá, že začíná hráč X'''

    move = 0

    for index in range(3):
        for i in range(3):
            if board[index][i] != ' ':
                move += 1

    if move % 2 == 0:
        int(input('Player X | Please enter your move number: '))
    else:
        int(input('Player O | Please enter your move number:'))
    



# Definice funkce pro kontrolu vítěze

def winner(board):

    # vítěz je X
    if (board[0][0] == board[0][1] == board[0][2] == "X" or
        board[1][0] == board[1][1] == board[1][2] == "X" or
        board[2][0] == board[2][1] == board[2][2] == "X" or
        board[0][0] == board[1][0] == board[2][0] == "X" or
        board[0][1] == board[1][1] == board[2][1] == "X" or
        board[0][2] == board[1][2] == board[2][2] == "X" or
        board[0][0] == board[1][1] == board[2][2] == "X" or
        board[0][2] == board[1][1] == board[2][0] == "X"):
            
            print(separator)
            print('Congratulations, the player X WON!')
            print(separator)

    # vítěz je O
    elif (board[0][0] == board[0][1] == board[0][2] == "O" or
        board[1][0] == board[1][1] == board[1][2] == "O" or
        board[2][0] == board[2][1] == board[2][2] == "O" or
        board[0][0] == board[1][0] == board[2][0] == "O" or
        board[0][1] == board[1][1] == board[2][1] == "O" or
        board[0][2] == board[1][2] == board[2][2] == "O" or
        board[0][0] == board[1][1] == board[2][2] == "O" or
        board[0][2] == board[1][1] == board[2][0] == "O"):
            
            print(separator)
            print('Congratulations, the player O WON!')
            print(separator)
        
    else:
        print(separator)
        print("It's a draw!")
        print(separator)




















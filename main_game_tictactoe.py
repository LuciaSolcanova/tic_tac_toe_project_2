"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

TIC TAC TOE GAME

author: Lucia Solčanová
email: lucia.solcanova@gmail.com
discord: Lucka #0676
"""

import random
import time

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












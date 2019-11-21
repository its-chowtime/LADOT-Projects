# Chessboard

import numpy as np
import random

cols =['1','2','3','4','5','6','7','8']
rows = ['A','B','C','D','E','F','G','H']

# 8 x 8 chessboard
c_b = [['A1','A2','A3','A4','A5','A6','A7','A8'],
       ['B1','B2','B3','B4','B5','B6','B7','B8'],
       ['C1','C2','C3','C4','C5','C6','C7','C8'],
       ['D1','D2','D3','D4','D5','D6','D7','D8'],
       ['E1','E2','E3','E4','E5','E6','E7','E8'],
       ['F1','F2','F3','F4','F5','F6','F7','F8'],
       ['G1','G2','G3','G4','G5','G6','G7','G8'],
       ['H1','H2','H3','H4','H5','H6','H7','H8']]

# Visual chessboard
for xx in range(8):
    for yy in range(8):
        all_rows = rows[xx] + cols[yy]
        print(all_rows, end =' ')
    print()

# Chess pieces
chess_pieces = {'pawns':'Pw','knight':'Kn','bishop':'Bs','queen':'Qu','king':'Kg'}

# Function

def start():
    print('Enter a piece at starting point A1')
    userinput = input()
    c_b[0][0] = chess_pieces[userinput]
    print(c_b)
start()
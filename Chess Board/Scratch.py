# Chessboard

import numpy as np
import random

cols_alpha_index = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
rows_index_alpha = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H'}

# 8 x 8 chessboard - currently not using
c_b = [['A1','A2','A3','A4','A5','A6','A7','A8'],
       ['B1','B2','B3','B4','B5','B6','B7','B8'],
       ['C1','C2','C3','C4','C5','C6','C7','C8'],
       ['D1','D2','D3','D4','D5','D6','D7','D8'],
       ['E1','E2','E3','E4','E5','E6','E7','E8'],
       ['F1','F2','F3','F4','F5','F6','F7','F8'],
       ['G1','G2','G3','G4','G5','G6','G7','G8'],
       ['H1','H2','H3','H4','H5','H6','H7','H8']]
'''
for x in c_b:
    print()
    print(x)
'''
# Place knight in starting position

knight = 'Kn'
c_b[0][0] = knight
print(c_b)
'''
for x in c_b:
    c_b[0][0] = 'Kn'
    print()
    print(x)

def move():
'''

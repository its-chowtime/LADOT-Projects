import numpy as np

col = [0,1,2,3,4,5,6,7]
row = [7,6,5,4,3,2,1,0]

c_b = [['A1','A2','A3','A4','A5','A6','A7','A8'],
       ['B1','B2','B3','B4','B5','B6','B7','B8'],
       ['C1','C2','C3','C4','C5','C6','C7','C8'],
       ['D1','D2','D3','D4','D5','D6','D7','D8'],
       ['E1','E2','E3','E4','E5','E6','E7','E8'],
       ['F1','F2','F3','F4','F5','F6','F7','F8'],
       ['G1','G2','G3','G4','G5','G6','G7','G8'],
       ['H1','H2','H3','H4','H5','H6','H7','H8']]

#x = input('Enter a x coordinate: ')
#y = input('Enter a y coordinate: ')


# Choose starting point
x = col[0]
y = row[7]
'''
x = col[int(x)]
y = row[int(y)]
'''

current_pos = c_b[x][y]

c_b[x][y] = 'Kn' # Setting piece to position

# Move the piece
if current_pos == current_pos:
    x += 1
    y += 2
    c_b[x][y] = 'Kn'
    print(current_pos)
else:
    print('DID NOT WORK')

# Board visualization
for asd in c_b:
    print()
    print(asd)

def move():
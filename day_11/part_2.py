import intcode_computer as intcode
import numpy as np
import textwrap

BLACK = 0
WHITE = 1
BLACK_CHAR = ' '
WHITE_CHAR = '#'
TURN_LEFT = 0
TURN_RIGHT = 1

''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

computer = intcode.IntcodeComputer(content)

pos=(0,0)
# N 0
# E 1
# S 2
# W 3
direction = 0
tiles = {pos: WHITE}

while not computer.is_program_complete():
    cur_tile = tiles[pos] if pos in tiles else BLACK

    [new_tile, new_direction] = computer.execute_program(cur_tile)

    tiles[pos] = new_tile
    if new_direction == TURN_LEFT:
        direction = (direction - 1)%4
    else:
        direction = (direction + 1)%4

    if direction == 0:
        #N
        pos = (pos[0], pos[1] - 1)
    elif direction == 1:
        #E
        pos = (pos[0] + 1, pos[1])
    elif direction == 2:
        #S
        pos = (pos[0], pos[1] + 1)
    elif direction == 3:
        #W
        pos = (pos[0] - 1, pos[1])

min_x = min([x[0] for x in tiles.keys()])
max_x = max([x[0] for x in tiles.keys()])
min_y = min([x[1] for x in tiles.keys()])
max_y = max([x[1] for x in tiles.keys()])
cols = max_x - min_x
rows = max_y - min_y
print(rows, cols)

matrix = [      [tiles[(x,y)] if (x,y) in tiles else BLACK
                for x in range(min_x, max_x)]
            for y in range(min_y, max_y)]

result = np.array(matrix).reshape(rows*cols, 1)
result = [BLACK_CHAR if x == BLACK else WHITE_CHAR for x in result]
result = np.array(result).reshape(rows, cols)
[print(textwrap.fill(str(x), width=200)) for x in result]

# print("The toal number of panels is {}".format(total_panels))

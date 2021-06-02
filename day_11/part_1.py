import intcode_computer as intcode

BLACK = 0
WHITE = 1
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
tiles = {pos: BLACK}

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

total_panels = len(tiles)
print("The toal number of panels is {}".format(total_panels))

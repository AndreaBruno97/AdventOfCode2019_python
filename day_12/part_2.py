import re
import numpy as np

MOON_NUM = 4
D_NUM = 3

''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

initial_speeds = [[0 for x in range(D_NUM)] for y in range(MOON_NUM)]
initial_positions = [
    [int(x) for x in re.sub(r'[<> xyz=]', '', line).split(",")]
    for line in content.split("\n")
]

positions = [pos.copy() for pos in initial_positions]
speeds = [sp.copy() for sp in initial_speeds]

steps_num = 0

while True:
    steps_num += 1

    # Apply gravity
    for moon in range(MOON_NUM):
        for dir in range(D_NUM):
            speeds[moon][dir] += sum(
                                    np.sign([
                                          other_moon_pos[dir] - positions[moon][dir]
                                        for other_moon_pos in positions
                                    ]))
    # Apply speed
    for moon in range(MOON_NUM):
        for dir in range(D_NUM):
            positions[moon][dir] += speeds[moon][dir]

    if not steps_num%1000:
        print(str(steps_num))

    if not sum([
        positions[moon] != initial_positions[moon]
        for moon in range(MOON_NUM)
    ]) and not sum([
                speeds[moon] != initial_speeds[moon]
            for moon in range(MOON_NUM)
    ]):
        break

print("The number of steps is: " + str(steps_num))
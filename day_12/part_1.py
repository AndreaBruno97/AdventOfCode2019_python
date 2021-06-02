import re
import numpy as np

MOON_NUM = 4
D_NUM = 3
STEPS_NUM = 1000

''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

speeds = [[0 for x in range(D_NUM)] for y in range(MOON_NUM)]
positions = [
    [int(x) for x in re.sub(r'[<> xyz=]', '', line).split(",")]
    for line in content.split("\n")
]

for i in range(STEPS_NUM):
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

energy = sum([
    sum(
        [abs(x) for x in positions[moon]]
    ) * sum(
        [abs(x) for x in speeds[moon]]
    )
    for moon in range(MOON_NUM)
])

print("The total energy of the system is: " + str(energy))
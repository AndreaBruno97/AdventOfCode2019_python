import math
import sys

''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

asteroids = set()

for r, row in enumerate(content.split("\n")):
    for c, position in enumerate(list(row)):
        if position == "#":
            asteroids.add((c, r))

max_visible_asteroids = -sys.maxsize -1
for target_asteroid in asteroids:
    cur_set = set()
    for asteroid in asteroids:
        new_coord_0 = target_asteroid[0]-asteroid[0]
        new_coord_1 = target_asteroid[1]-asteroid[1]
        divisor = math.gcd(new_coord_0, new_coord_1)

        if divisor != 0:
            new_coord_0 = new_coord_0/divisor
            new_coord_1 = new_coord_1/divisor
        else:
            new_coord_0 = 0
            new_coord_1 = 0

        cur_set.add((new_coord_0, new_coord_1))

    visible_asteroids_num = len(cur_set) - 1

    if visible_asteroids_num > max_visible_asteroids:
        max_visible_asteroids = visible_asteroids_num

print("The maximum number of visible asteroids is: " + str(max_visible_asteroids))
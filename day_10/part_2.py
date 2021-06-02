import math
import sys

TARGET_NUM = 200

''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

asteroids = set()
best_asteroid = None
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
        best_asteroid = target_asteroid

asteroids = [(x[0] - best_asteroid[0], best_asteroid[1]-x[1]) for x in asteroids]
asteroids.remove((0,0))
dict_asteroids = {}

for asteroid in asteroids:

    divisor = math.gcd(asteroid[0], asteroid[1])

    if divisor != 0:
        new_coord_0 = asteroid[0] / divisor
        new_coord_1 = asteroid[1] / divisor
    else:
        new_coord_0 = 0
        new_coord_1 = 0

    reduced_coord = (new_coord_0, new_coord_1)

    if reduced_coord in dict_asteroids:
        dict_asteroids[reduced_coord].append(asteroid)
    else:
        dict_asteroids[reduced_coord] = [asteroid]

for key, value in dict_asteroids.items():
    dict_asteroids[key] = sorted(value, key=lambda x: (x[0] ** 2) + (x[1] ** 2))

dict_keys = sorted(list(dict_asteroids.keys()), key=
lambda x: -(math.atan(x[1]/x[0])
            - ((math.pi/2) * (x[0] < 0))
            - ((math.pi/2) * (x[0] < 0 and x[1] > 0)))
        if x[0] != 0
        else (-sys.maxsize if x[1]>0 else math.pi/2))
cur_asteroids_num = 0
cur_asteroid = None

while cur_asteroids_num < TARGET_NUM:
    for key in dict_keys:
        if len(dict_asteroids[key]) == 0:
            continue

        cur_asteroid = dict_asteroids[key].pop(0)
        cur_asteroids_num += 1

        if cur_asteroids_num == TARGET_NUM:
            break

cur_asteroid = (best_asteroid[0] + cur_asteroid[0], best_asteroid[1] - cur_asteroid[1])
final_code = ( 100 * cur_asteroid[0] ) + cur_asteroid[1]

print("The final code is: " + str(final_code))
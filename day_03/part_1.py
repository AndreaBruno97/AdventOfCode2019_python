''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

LEFT = "L"
RIGHT = "R"
UP = "U"
DOWN = "D"

path = [x.split(",") for x in content.split("\n")]
path_set = [set() for x in path]

for i in range(len(path)):
    x = 0
    y = 0

    for instruction in path[i]:
        direction = instruction[0]
        length = int(instruction[1:])

        steps = []
        if direction == LEFT:
            steps = [(new_x, y) for new_x in range(x-length, x)]
            x = x-length
        elif direction == RIGHT:
            steps = [(new_x, y) for new_x in range(x+1, x+length+1)]
            x = x+length
        elif direction == UP:
            steps = [(x, new_y) for new_y in range(y+1, y+length+1)]
            y = y+length
        elif direction == DOWN:
            steps = [(x, new_y) for new_y in range(y-length, y)]
            y = y-length

        [path_set[i].add(x) for x in steps]

result = [abs(x[0])+abs(x[1]) for x in path_set[0].intersection(path_set[1])]
result.sort()
print("The nearest intersection has distance: " + str(result[0]))
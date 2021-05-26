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
path_times = [{} for x in path]

for i in range(len(path)):
    x = 0
    y = 0
    time = 1

    for instruction in path[i]:
        direction = instruction[0]
        length = int(instruction[1:])

        steps = []
        if direction == LEFT:
            steps = [(new_x, y) for new_x in range(x - length, x)[::-1]]
            x = x - length
        elif direction == RIGHT:
            steps = [(new_x, y) for new_x in range(x + 1, x + length + 1)]
            x = x + length
        elif direction == UP:
            steps = [(x, new_y) for new_y in range(y + 1, y + length + 1)]
            y = y + length
        elif direction == DOWN:
            steps = [(x, new_y) for new_y in range(y - length, y)[::-1]]
            y = y - length

        for step in steps:
            path_set[i].add(step)
            if step not in path_times[i]:
                path_times[i][step] = time
            time += 1

result = [path_times[0][x] + path_times[1][x] for x in path_set[0].intersection(path_set[1])]
result.sort()

print("The first intersection occurs at time: " + str(result[0]))

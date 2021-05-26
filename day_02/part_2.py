''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()
program = [int(x) for x in content.split(",")]
ADD = 1
MULTIPLY = 2
STOP = 99
TARGET = 19690720
RANGE = 100

original_program = program.copy()

for noun in range(RANGE):
    for verb in range(RANGE):
        program = original_program.copy()

        program[1] = noun
        program[2] = verb

        index = 0
        while program[index] != STOP:
            opcode, a, b, c = program[index:index + 4]

            if opcode == ADD:
                program[c] = program[a] + program[b]
            else:
                program[c] = program[a] * program[b]

            index += 4

        if program[0] == TARGET: break
    if program[0] == TARGET: break

print("100 * noun + verb: " + str((100 * noun) + verb))

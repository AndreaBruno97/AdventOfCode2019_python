''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()
program = [int(x) for x in content.split(",")]
ADD = 1
MULTIPLY = 2
STOP = 99

program[1] = 12
program[2] = 2

index = 0
while program[index] != STOP:
    opcode, a, b, c = program[index:index+4]

    if opcode == ADD:
        program[c] = program[a] + program[b]
    else:
        program[c] = program[a] * program[b]

    index += 4

print("The value left at position 0 is: " + str(program[0]))

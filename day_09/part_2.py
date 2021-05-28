import intcode_computer as intcode

''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

computer = intcode.IntcodeComputer(content)
result = computer.execute_program(2)[0]

print("The coordinate is: " + str(result))
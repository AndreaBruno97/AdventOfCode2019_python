import intcode_computer as intcode

''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

input = [5]
diagnostic_code = intcode.execute_program(content, input)[1][0]
print("The diagnostic code is: " + str(diagnostic_code))

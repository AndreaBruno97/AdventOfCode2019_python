import intcode_computer as intcode
import itertools
import sys

AMP_NUM = 5


''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

phase_sequence_list = itertools.permutations(range(AMP_NUM, 2 * AMP_NUM))

max_output = -sys.maxsize - 1
for phase_sequence in phase_sequence_list:
    amps = []

    for phase in phase_sequence:
        cur_computer = intcode.IntcodeComputer(content)
        amps.append(cur_computer)
        cur_computer.execute_program(phase)
    cur_output = 0

    while len(amps) > sum([x.is_program_complete() for x in amps]):
        for amp in amps:
            cur_output = amp.execute_program(cur_output)

    if max_output < cur_output:
        max_output = cur_output

print("The maximum output is: " + str(max_output))

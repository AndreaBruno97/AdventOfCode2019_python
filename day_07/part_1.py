import old_intcode_computer as intcode
import itertools
import sys

AMP_NUM = 5

def call_program(content, inputs):
    return intcode.execute_program(content, inputs)[1][-1]


''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

phase_sequence_list = itertools.permutations(range(AMP_NUM))

max_output = -sys.maxsize -1
for phase_sequence in phase_sequence_list:
    cur_output = 0

    for phase in phase_sequence:
        cur_output = call_program(content, [phase, cur_output])

    if max_output < cur_output:
        max_output = cur_output

print("The maximum output is: " + str(max_output))
ADD = 1
MULTIPLY = 2
INPUT = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
STOP = 99

POSITION_MODE = 0
IMMEDIATE_MODE = 1

def execute_program(content, input):
    def add(params):
        [(a,a_mode), (b, b_mode), (c, c_mode)] = params

        # if c_mode == IMMEDIATE_MODE:
        #     return 1

        first = program[a] if a_mode == POSITION_MODE else a
        second = program[b] if b_mode == POSITION_MODE else b
        program[c] = first + second

    def multiply(params):
        [(a,a_mode), (b, b_mode), (c, c_mode)] = params

        # if c_mode == IMMEDIATE_MODE:
        #     return 1

        first = program[a] if a_mode == POSITION_MODE else a
        second = program[b] if b_mode == POSITION_MODE else b
        program[c] = first * second

    def get_input(params):
        [(a, a_mode)] = params

        # if a_mode == IMMEDIATE_MODE:
        #     return 1

        program[a] = input[0]

    def set_output(params):
        [(a, a_mode)] = params
        return program[a] if a_mode == POSITION_MODE else a

    def jump_if_true(params):
        [(a, a_mode), (b, b_mode)] = params
        first = program[a] if a_mode == POSITION_MODE else a
        second = program[b] if b_mode == POSITION_MODE else b

        if first != 0:
            return second

    def jump_if_false(params):
        [(a, a_mode), (b, b_mode)] = params
        first = program[a] if a_mode == POSITION_MODE else a
        second = program[b] if b_mode == POSITION_MODE else b

        if first == 0:
            return second

    def less_than(params):
        [(a, a_mode), (b, b_mode), (c, c_mode)] = params
        # if c_mode == IMMEDIATE_MODE:
        #     return 1

        first = program[a] if a_mode == POSITION_MODE else a
        second = program[b] if b_mode == POSITION_MODE else b

        program[c] = int(first < second)

    def equals(params):
        [(a, a_mode), (b, b_mode), (c, c_mode)] = params
        # if c_mode == IMMEDIATE_MODE:
        #     return 1

        first = program[a] if a_mode == POSITION_MODE else a
        second = program[b] if b_mode == POSITION_MODE else b

        program[c] = int(first == second)

    codes = {
        ADD: {
            "num": 3,
            "func": add
        },
        MULTIPLY: {
            "num": 3,
            "func": multiply
        },
        INPUT: {
            "num": 1,
            "func": get_input
        },
        OUTPUT: {
            "num": 1,
            "func": set_output
        },
        JUMP_IF_TRUE: {
            "num": 2,
            "func": jump_if_true
        },
        JUMP_IF_FALSE: {
            "num": 2,
            "func": jump_if_false
        },
        LESS_THAN: {
            "num": 3,
            "func": less_than
        },
        EQUALS: {
            "num": 3,
            "func": equals
        },
        STOP: {
            "num": 0,
            "func": None
        },
    }

    program = [int(x) for x in content.split(",")]

    index = 0
    output = []
    while program[index] != STOP:
        instruction = program[index]
        opcode = instruction % 100

        cur_function = codes[opcode]["func"]
        cur_param_num = codes[opcode]["num"]

        parameters = []
        mode_list = int(instruction/100)
        for i in range(index + 1, index + cur_param_num + 1):
            parameters.append((program[i], mode_list % 10))
            mode_list = int(mode_list/10)

        next_index = index + cur_param_num + 1

        cur_result = cur_function(parameters)
        if opcode == OUTPUT:
            output.append(cur_result)
        elif opcode in [JUMP_IF_TRUE, JUMP_IF_FALSE] and cur_result:
            next_index = cur_result

        index = next_index
    return program, output

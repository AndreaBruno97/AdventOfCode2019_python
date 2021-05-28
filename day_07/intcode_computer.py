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


def add(self, params):
    [(a, a_mode), (b, b_mode), (c, c_mode)] = params

    # if c_mode == IMMEDIATE_MODE:
    #     return 1

    first = self.program[a] if a_mode == POSITION_MODE else a
    second = self.program[b] if b_mode == POSITION_MODE else b
    self.program[c] = first + second


def multiply(self, params):
    [(a, a_mode), (b, b_mode), (c, c_mode)] = params

    # if c_mode == IMMEDIATE_MODE:
    #     return 1

    first = self.program[a] if a_mode == POSITION_MODE else a
    second = self.program[b] if b_mode == POSITION_MODE else b
    self.program[c] = first * second


def get_input(self, params):
    [(a, a_mode)] = params

    # if a_mode == IMMEDIATE_MODE:
    #     return 1

    if not self.is_input_consumed:
        self.program[a] = self.input
        self.is_input_consumed = True


def set_output(self, params):
    [(a, a_mode)] = params
    return self.program[a] if a_mode == POSITION_MODE else a


def jump_if_true(self, params):
    [(a, a_mode), (b, b_mode)] = params
    first = self.program[a] if a_mode == POSITION_MODE else a
    second = self.program[b] if b_mode == POSITION_MODE else b

    if first != 0:
        return second


def jump_if_false(self, params):
    [(a, a_mode), (b, b_mode)] = params
    first = self.program[a] if a_mode == POSITION_MODE else a
    second = self.program[b] if b_mode == POSITION_MODE else b

    if first == 0:
        return second


def less_than(self, params):
    [(a, a_mode), (b, b_mode), (c, c_mode)] = params
    # if c_mode == IMMEDIATE_MODE:
    #     return 1

    first = self.program[a] if a_mode == POSITION_MODE else a
    second = self.program[b] if b_mode == POSITION_MODE else b

    self.program[c] = int(first < second)


def equals(self, params):
    [(a, a_mode), (b, b_mode), (c, c_mode)] = params
    # if c_mode == IMMEDIATE_MODE:
    #     return 1

    first = self.program[a] if a_mode == POSITION_MODE else a
    second = self.program[b] if b_mode == POSITION_MODE else b

    self.program[c] = int(first == second)


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


class IntcodeComputer:
    def __init__(self, content):
        self.content = content
        self.program = [int(x) for x in content.split(",")]
        self.index = 0
        self.input = None
        self.is_complete = False
        self.is_input_consumed = True

    def is_program_complete(self):
        return self.is_complete

    def execute_program(self, input):
        if self.is_complete: return

        if input is not None:
            self.is_input_consumed = False
            self.input = input
        output = None

        while self.program[self.index] != STOP:
            instruction = self.program[self.index]
            opcode = instruction % 100

            if opcode == INPUT and self.is_input_consumed:
                return output

            cur_function = codes[opcode]["func"]
            cur_param_num = codes[opcode]["num"]

            parameters = []
            mode_list = int(instruction / 100)
            for i in range(self.index + 1, self.index + cur_param_num + 1):
                parameters.append((self.program[i], mode_list % 10))
                mode_list = int(mode_list / 10)

            next_index = self.index + cur_param_num + 1

            cur_result = cur_function(self, parameters)

            if opcode in [JUMP_IF_TRUE, JUMP_IF_FALSE] and cur_result:
                next_index = cur_result
            elif opcode == OUTPUT:
                output = cur_result

            self.index = next_index

        self.is_complete = True
        return output

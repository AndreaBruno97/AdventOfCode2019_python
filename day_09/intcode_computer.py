ADD = 1
MULTIPLY = 2
INPUT = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
ADJUST_RELATIVE_BASE = 9
STOP = 99

POSITION_MODE = 0
IMMEDIATE_MODE = 1
RELATIVE_MODE = 2

def read_memory(self, a):
    if a < len(self.program):
        return self.program[a]
    elif a in self.outer_memory:
        return self.outer_memory[a]
    else:
        return 0

def write_memory(self, index, value):
    if index < len(self.program):
        self.program[index] = value
    else:
        self.outer_memory[index] = value

def get_param(self, a, a_mode):
    switcher = {
        POSITION_MODE: lambda x: read_memory(self, x),
        IMMEDIATE_MODE: lambda x: x,
        RELATIVE_MODE: lambda x: read_memory(self, x + self.relative_base)
    }
    return switcher[a_mode](a)

def set_param(self, index, a_mode, a):
    switcher = {
        POSITION_MODE: lambda x: write_memory(self, index, x),
        # IMMEDIATE_MODE: ERROR,
        RELATIVE_MODE: lambda x: write_memory(self, index + self.relative_base, x)
    }
    switcher[a_mode](a)

def add(self, params):
    [(a, a_mode), (b, b_mode), (c, c_mode)] = params

    first = get_param(self, a, a_mode)
    second = get_param(self, b, b_mode)

    set_param(self, c, c_mode, first + second)

def multiply(self, params):
    [(a, a_mode), (b, b_mode), (c, c_mode)] = params

    first = get_param(self, a, a_mode)
    second = get_param(self, b, b_mode)
    set_param(self, c, c_mode, first * second)


def get_input(self, params):
    [(a, a_mode)] = params

    if not self.is_input_consumed:
        set_param(self, a, a_mode, self.input)
        self.is_input_consumed = True


def set_output(self, params):
    [(a, a_mode)] = params
    return get_param(self, a, a_mode)


def jump_if_true(self, params):
    [(a, a_mode), (b, b_mode)] = params
    first = get_param(self, a, a_mode)
    second = get_param(self, b, b_mode)

    if first != 0:
        return second


def jump_if_false(self, params):
    [(a, a_mode), (b, b_mode)] = params
    first = get_param(self, a, a_mode)
    second = get_param(self, b, b_mode)

    if first == 0:
        return second


def less_than(self, params):
    [(a, a_mode), (b, b_mode), (c, c_mode)] = params

    first = get_param(self, a, a_mode)
    second = get_param(self, b, b_mode)

    set_param(self, c, c_mode, int(first < second))


def equals(self, params):
    [(a, a_mode), (b, b_mode), (c, c_mode)] = params

    first = get_param(self, a, a_mode)
    second = get_param(self, b, b_mode)

    set_param(self, c, c_mode, int(first == second))


def adjust_relative_base(self, params):
    [(a, a_mode)] = params

    self.relative_base += get_param(self, a, a_mode)

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
    ADJUST_RELATIVE_BASE: {
        "num": 1,
        "func": adjust_relative_base
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
        self.relative_base = 0
        self.input = None
        self.is_complete = False
        self.is_input_consumed = True
        self.outer_memory = {}

    def is_program_complete(self):
        return self.is_complete

    def execute_program(self, input):
        if self.is_complete: return

        if input is not None:
            self.is_input_consumed = False
            self.input = input
        output = []

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

            if opcode in [JUMP_IF_TRUE, JUMP_IF_FALSE] and cur_result is not None:
                next_index = cur_result
            elif opcode == OUTPUT:
                output.append(cur_result)

            self.index = next_index

        self.is_complete = True
        return output

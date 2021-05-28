import numpy as np
import textwrap

ROWS = 6
COLS = 25

BLACK = u"\u25A0"
WHITE = " "


''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

image = [int(x) for x in content]

num_layers = int(len(image) / (ROWS * COLS))
layers = np.array(image).reshape((num_layers, ROWS, COLS))

layers = np.moveaxis(layers, 0, -1).reshape(ROWS*COLS, num_layers)

message_array = [x[x != 2][0] for x in layers]
message_array = [BLACK if x else WHITE for x in message_array]
message = np.array(message_array).reshape(ROWS, COLS)

print("The final message is: ")
[print(textwrap.fill(str(x), width=200)) for x in message]
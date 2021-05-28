import numpy as np

ROWS = 6
COLS = 25

''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

image = [int(x) for x in content]

num_layers = int(len(image) / (ROWS * COLS))
layers = np.array(image).reshape((num_layers, ROWS, COLS))

min_zeros_layer = sorted(layers, key=lambda x: np.count_nonzero(x == 0))[0]
num_1 = np.count_nonzero(min_zeros_layer == 1)
num_2 = np.count_nonzero(min_zeros_layer == 2)

total = num_1 * num_2

print("The total value is: " + str(total))
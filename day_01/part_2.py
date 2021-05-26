def compute_fuel(start_fuel):
    total_fuel = 0
    cur_delta = start_fuel

    while cur_delta > 0:
        cur_delta = int(cur_delta/3) - 2
        if cur_delta > 0: total_fuel += cur_delta

    return total_fuel

''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

masses = [int(x) for x in content.split("\n")]
total = sum([compute_fuel(x) for x in masses])

print("The sum of the fuel requirements is: " + str(total))
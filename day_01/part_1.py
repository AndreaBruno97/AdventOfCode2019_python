''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

masses = [int(x) for x in content.split("\n")]
total = sum([int(x/3)-2 for x in masses])

print("The sum of the fuel requirements is: " + str(total))
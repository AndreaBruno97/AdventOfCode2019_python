''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

total = 0
for i in range(137683, 596254):
    cur_num = [int(x) for x in str(i)]
    if not sum([cur_num[i - 1] == cur_num[i] for i in range(1, len(cur_num))]):
        continue

    if sum([cur_num[i - 1] > cur_num[i] for i in range(1, len(cur_num))]):
        continue

    total+=1

print("There total number of values that satisfy the request is: " + str(total))
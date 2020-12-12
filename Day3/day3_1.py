import numpy as np

#comments parameter needs to be set to something else otherwise loadtxt will take # as comments and cut string
input = np.loadtxt("Day3/input.txt", dtype=str, comments="-")

#need static 300 lines because somehow len(input) returns 323 instead of 300
map = np.zeros((len(input),len(input[0])),str)

for i, element in enumerate(input):
    for j, element2 in enumerate(input[i]):
        map[i][j] = element2

row = 0
col = 0
row_incr = 1
col_incr = 3
tree = '#'
count = 0

while (row <= len(map) - 1):
    if col > len(map[0]) - 1:
        map = np.append(map,map,axis=1)
    if map[row][col] == tree:
        count += 1
    
    row += row_incr
    col += col_incr

print('Encountered trees: ' + str(count))
import numpy as np

def checkTrees(map, row_incr, col_incr, tree_symbol):
    row = 0
    col = 0
    count = 0

    while (row <= len(map) - 1):
        if col > len(map[0]) - 1:
            map = np.append(map,map,axis=1)
        if map[row][col] == tree_symbol:
            count += 1
    
        row += row_incr
        col += col_incr

    return count

#comments parameter needs to be set to something else otherwise loadtxt will take # as comments and cut string
input = np.loadtxt("Day3/input.txt", dtype=str, comments="-")

#need static 300 lines because somehow len(input) returns 323 instead of 300
map = np.zeros((len(input),len(input[0])),str)

for i, element in enumerate(input):
    for j, element2 in enumerate(input[i]):
        map[i][j] = element2

route1 = checkTrees(map, 1, 1, '#')
route2 = checkTrees(map, 1, 3, '#')
route3 = checkTrees(map, 1, 5, '#')
route4 = checkTrees(map, 1, 7, '#')
route5 = checkTrees(map, 2, 1, '#')

result = route1 * route2 * route3 * route4 * route5

print('Route 1: ' + str(route1))
print('Route 2: ' + str(route2))
print('Route 3: ' + str(route3))
print('Route 4: ' + str(route4))
print('Route 5: ' + str(route5))
print('Result: ' + str(result))
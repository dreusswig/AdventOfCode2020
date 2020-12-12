import numpy as np

input = np.loadtxt("Day2/input.txt", dtype=str)

limits = []
letter = []
password = []
count = 0

# Split input into limits, letter and password
for i, element in enumerate(input):
    limits.append(input[i,0].split('-'))
    letter.append(input[i,1])
    password.append(input[i,2])


for j, element in enumerate(password):
    occurences = element.count(letter[j][0])
    if int(limits[j][0]) <= occurences and occurences <= int(limits[j][1]):
        count += 1

print('Number of valid passwords: ' + str(count))
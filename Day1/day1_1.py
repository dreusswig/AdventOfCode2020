import numpy as np

input = np.loadtxt("Day1/input.txt", dtype=int)

for i, num1 in enumerate(input):
    done = 0
    for num2 in input[i+1:len(input)-1]:
        if num1 + num2 == 2020:
            done = 1
            break
    if done == 1:
        break

validate = num1+num2
result = num1*num2

print(str(num1) + ' + ' + str(num2) + ' = ' + str(validate))
print(str(num1) + ' * ' + str(num2) + ' = ' + str(result))
import numpy as np

input = np.loadtxt("Day1/input.txt", dtype=int)

for i, num1 in enumerate(input):
    done = 0
    for j, num2 in enumerate(input[i+1:len(input)-1]):
        for num3 in input[j+1:len(input)-1]:
            if num1 + num2 + num3 == 2020:
                done = 1
                break
        if done == 1:
            break
    if done == 1:
        break

validate = num1+num2+num3
result = num1*num2*num3

print(str(num1) + ' + ' + str(num2) + ' + ' + str(num3) + ' = ' + str(validate))
print(str(num1) + ' * ' + str(num2) + ' * ' + str(num3) + ' = ' + str(result))
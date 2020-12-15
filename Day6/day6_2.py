import numpy as np
from functions import countSameLetters

with open ("Day6/input.txt") as f: 
    input = f.readlines()

groupanswers = []
tmp_groupanswer = []

for line in input:
    if len(line) <= 1:
        groupanswers.append(tmp_groupanswer)
        tmp_groupanswer = []
    else:
        tmp_groupanswer.append(line.replace("\n", ""))
groupanswers.append(tmp_groupanswer)

sum = 0
for element in groupanswers:
    test, count = countSameLetters(element)
    sum += count

print("Everyone answered yes to " + str(sum) + " questions.")
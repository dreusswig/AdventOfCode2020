import numpy as np
from functions import countDifferentLetters

with open ("Day6/input.txt") as f: 
    input = f.readlines()

groupanswers = []
tmp_groupanswer = ''

for line in input:
    if len(line) <= 1:
        groupanswers.append(tmp_groupanswer)
        tmp_groupanswer = ''
    else:
        tmp_groupanswer = tmp_groupanswer + line.replace("\n", "")

groupanswers.append(tmp_groupanswer)

sum = 0

for element in groupanswers:
    characters, count = countDifferentLetters(element)
    sum += count

print("Anyone answered yes to " + str(sum) + " questions.")
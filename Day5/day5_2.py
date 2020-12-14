import numpy as np
from functions import divEtImp

input = np.loadtxt("Day5/input.txt", dtype=str)

ids = []

for seat in input:
    row = divEtImp(seat[0:7],'F','B')
    col = divEtImp(seat[7:10],'L','R')
    seatID = row * 8 + col
    ids.append(seatID)

for id in ids:
    if id + 2 in ids and not id + 1 in ids:
        my_seatID = id + 1

print("My Seat ID is: " + str(my_seatID))
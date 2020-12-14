import numpy as np
from functions import divEtImp

max_seatID = 0
cor_seat = ''

input = np.loadtxt("Day5/input.txt", dtype=str)

for seat in input:
    row = divEtImp(seat[0:7],'F','B')
    col = divEtImp(seat[7:10],'L','R')
    max_seatID_tmp = row * 8 + col
    if max_seatID_tmp > max_seatID:
        max_seatID = max_seatID_tmp
        cor_seat = seat


print("The maximum seat-ID on the plane is: " + str(max_seatID))
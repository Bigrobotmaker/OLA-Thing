total = 0
ArrayTwoD = [3,6,7],[4,8,1],[9,3,8]
for i in range (0,3):
    for j in range (0,3):
        total = ArrayTwoD[i][j] + total
print(total)
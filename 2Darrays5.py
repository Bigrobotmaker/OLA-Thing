area = 0
perimeter = 0
img = [0,0,0,0,0,0,0,],[0,0,0,1,0,0,0,],[0,0,1,1,1,0,0,],[0,1,1,1,1,1,0,],[0,0,1,1,1,0,0,],[0,0,0,1,0,0,0,],[0,0,0,0,0,0,0,]
for i in range (0,7):
    for j in range (0,7):
        area = img[i][j] + area
print("area =", area)
img2 = [0,0,0,0,0,0,0,],[0,0,0,1,0,0,0,],[0,0,1,0,1,0,0,],[0,1,0,0,0,1,0,],[0,0,1,0,1,0,0,],[0,0,0,1,0,0,0,],[0,0,0,0,0,0,0,]
for i in range (0,7):
    for j in range (0,7):
        perimeter = img2[i][j] + perimeter
print("the ratio is", area, ":", perimeter)
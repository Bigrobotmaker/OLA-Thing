# def C(n,k):
#     if n == 0 and k == 0:
#         return (1)
#     elif n < 0 or k < 0:
#         return (0)
#     previous = C(n-1,k-1)
#     current = previous + C(n-1,k)
#     return current
# print(C(1,1))
n = 40
k = 20
b = [[0]*41 for i in range(41)]
for i in b:
    for a in range(len(i)):
        print(b[i][a])
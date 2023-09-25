import random
s = int(input("what is the seed?"))
random.seed(s)
multiplier = 56
offset = 82
modulus = 37
for i in range(0,30):
    s = int(multiplier * s + offset) % modulus
    print(s) 
import random
lines = 0
f = open('geogquiz.txt')
lin = f.readlines()
for line in lin:
    lines = lines + 1
r = random.randint(0,lines)
i = lin[r].split(',')
country = i[0]
print('what is the capital of',country + '? ')
ans = input()
if ans == i[1]:
    print('Well done! you got it right!')
else:
    print('Incorrect answer, the correct answer is', i[1])
f.close()
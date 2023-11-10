import random
lines = 0
questions = 0
correct = 0
passes = 0
hints = 0
f = open('geogquiz.txt')
lin = f.readlines()
for line in lin:
    lines = lines + 1
while questions < 10:
    r = random.randint(0,lines)
    i = lin[r].split(',')
    country = i[0]
    print('question', questions + 1,'what is the capital of',country + '? ')
    ans = input()
    if ans == i[1].strip():
        print('Well done! you got it right!')
        questions = questions + 1
        correct = correct + 1
    elif ans == 'pass' and passes < 5:
        print('it was', i[1])
        passes = passes + 1
        print('you have used', passes, 'out of five passes')
    elif ans == 'hint' and hints == 0:
        print('your hint is that the first letter is', i[1][0],'you cannot pass')
        newans = input()
        if newans == i[1]:
            print('Well done! you got it right, your only hint has been used')
            hints = hints + 1
            questions = questions + 1
        else:
            print('Incorrect answer, the correct answer is', i[1])
            questions = questions + 1
            hints = hints + 1
    else:
        print('Incorrect answer, the correct answer is', i[1])
        questions = questions + 1
if correct == 10:
    print('wow you got them all!')
else:
    print('you got', ((correct/10)*100),'percent right, try to go for a higher score next time')
f.close()
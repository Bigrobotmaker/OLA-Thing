#name = input('what is the name of the text file ')
#f = open(name)
#txt = f.read()
#new = input('what would be the name of the new file ')
#n = open(new, "w")
#for w in txt:
#    n.write(w)
#f.close()
#n.close()

# f = open('gambling')
# runs = 1
# r = f
# for line in r:
#    print(runs,line.strip())
#    runs = runs+1

# f = open('Dict5LetterWords.txt')
# for line in f:
#    if 'oe' in line:
#        print(line.strip())

# f = open('sowpods.txt')
# substr = input('what substring would you like to search ')
# for line in f:
#     if substr in line:
#         print(line.strip())

import random
f = open('countriescapitals.txt')
r = random.randint(0,len)
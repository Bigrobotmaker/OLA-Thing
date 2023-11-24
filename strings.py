#strin = str(input('please enter your string '))
#print('the string is',len(strin), 'characters long')

# wrd = input('please enter a word ')
# a = len(wrd)
# if wrd[0] == wrd[a-1]:
#     print('the first and last letters are the same')
# else:
#     print('the first and last letters are not the same')

#wrd1 = input('first word ')
#wrd2 = input('second word ')
#print(wrd1[len(wrd1)-3] + wrd1[len(wrd1)-2] + wrd1[len(wrd1)-1] + wrd2[0] + wrd2[1] + wrd2[2])

# words = input('please input a sentence ')
# words = words.split(' ')
# print('it has', len(words), 'words')

master = input('what is the master word? ')
test = input('what is the test word? ')
if len(test) > len(master):
    print('test word too long, try again')
else:
    if test in master:
        print('the test word is in the master word')
    else:
        print('the test word is not in the master word')
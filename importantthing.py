#def six(n):
#    if n == 0:
#        return 1
#    return (six(n-1)*2) % 1000000
#print(six(300)
def sixbutreallyreallyfast(n):
    if n == 0:
        return 1
    if n%2 ==1:
        return(sixbutreallyreallyfast(n-1)*2)%1000000
    root = sixbutreallyreallyfast(n//2)
    return(root*root)%1000000
print(sixbutreallyreallyfast(123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100))
def factorial(num):
#    runs = 0
#    total = 1
#    while runs != num-1:
#        total = total * (num-runs)
#        runs = runs + 1
#    return(total)
#print(factorial(50))
    if num == 0:
        return 1
    previous = factorial(num-1 )
    current = previous * num
    return(current)
print(factorial(5))
number = input("enter a number ")
jeff = False
try:
    while jeff == False:
        Value = int(number)
except KeyboardInterrupt:
    Value = 0
print(Value)
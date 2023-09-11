import random
money = 100
going = "yes"
while going == "yes":
    print("you have", money, "dollars left")
    bet = input("what would you like to bet? even, odd, small, medium, large or leave? ")
    if bet == "even" or bet == "Even":
        num = int(input("how much would you like to bet? "))
        while num > money:
            num = int(input("please bet no more than the amount of money you have "))
        roll = random.randint(1,36)
        if (roll)%2 == 0:
            print("you won!!")
            money = money + (num)
        else:
            print("oh no! you lost")
            money = money - num
    if bet == "odd" or bet == "Odd":
        num = int(input("how much would you like to bet? "))
        while num > money:
            num = int(input("please bet no more than the amount of money you have "))
        roll = random.randint(1,36)
        if (roll)%2 == 1:
            print("the roll was", roll, "!")
            print("You won!")
            money = money + (num)
        else:
            print("the roll was", roll, "!")
            print("Oh no! you lost")
            money = money - num
    #if bet == "small":
    
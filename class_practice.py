class calculate:
    def __init__(self, num1, num2):
        self.num1 = 1
        self.num2 = 1
    def add(self):
        print(self.num1 + self.num2)
    def subtract(self):
        print(self.num1 - self.num2)
    def multiply(self):
        print(self.num1*self.num2)
    def divide(self):
        print(self.num1//self.num2)
    def factorial(self):
        numb = 1
        for i in range(num):
            numb *= i+1
        print(numb)
    def changenumbers(self):
        self.num1 = int(input('first number '))
        self.num2 = int(input('second number '))
a = calculate(1, 1)
opp = input('what operation would you like to do? ')
if opp == 'add' or opp == 'Add':
    a.changenumbers()
    a.add()
if opp == 'subtract' or opp == 'Subtract':
    a.changenumbers()
    a.subtract()
if opp == 'multiply' or opp == 'Multiply':
    a.changenumbers()
    a.multiply()
if opp == 'divide' or opp == 'Divide':
    a.changenumbers()
    a.divide()
if opp == 'factorial' or opp == 'Factorial':
    num = int(input('what number would you like to use? '))
    a.factorial()
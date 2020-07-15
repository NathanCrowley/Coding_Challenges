class Calculator:
    def __init__(self):
        pass

    def plus(self,x,y):
        return x + y

    def minus(self,x,y):
        return x - y

    def multiply(self,x,y):
        return x*y

    def divide(self,x,y):
        return x//y

#--------------------------------TEST-----------------------
calculator = Calculator()
print(calculator.plus(10,5))
print(calculator.minus(10,5))
print(calculator.multiply(10,5))
print(calculator.divide(10,5))
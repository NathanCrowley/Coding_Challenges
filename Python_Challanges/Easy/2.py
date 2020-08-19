'''
3/7/2020
            WORKING.
'''

def Return_factorial(x):
    counter = x
    for int in range(1,x):
        counter = counter*int
    print("{}! = {}".format(x,counter))

user = int(input("Enter number to return Factorial >>> "))
Return_factorial(user)
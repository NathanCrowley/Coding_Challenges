'''
Nathan Crowley - 14/7/2020

function that swaps int with how many times it appears in the inputed integer.
'''
def keepingCount(num):
    num = str(num)
    answer = ''
    for integer in num:
        answer += count_int(integer,num)
    answer = int(answer)
    print(answer)


def count_int(int,string):  #function to count how many occurances of int in string
    count = 0
    for x in string:
        if x == int:
            count += 1
    return str(count)       #return as a string to append later on

# Test-------------------------
keepingCount(221333)
keepingCount(136116)
keepingCount(2)


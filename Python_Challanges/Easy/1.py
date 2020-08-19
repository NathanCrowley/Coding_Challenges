'''

3/7/2020
            WORKING.
'''


def Inequaltity_Signs(a,sign,b):
    if sign == '<':
        if a < b:
            return True
        return False
    elif sign == '>':
        if a > b:
            return True
        return False
    elif sign == '=':
        if a == b:
            return True
        return False
    else:
        return "Error your input is incorrect!!!!!"


print(Inequaltity_Signs(12,'<',4))
print(Inequaltity_Signs(40,'>',9))
print(Inequaltity_Signs(10,'=',10))
print(Inequaltity_Signs(55,'<',20))

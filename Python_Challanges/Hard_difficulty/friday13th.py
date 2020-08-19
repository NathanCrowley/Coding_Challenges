'''
given month and years return whether that month contains a Friday 13th.
'''
import datetime

def has_friday13(month,year):
    day = 13
    x = datetime.datetime(year,month,day)
    #Y = x.strftime('%a')
    if x.strftime('%a') == 'Fri':   #check if the given month's 13th day is a friday or not.
        return True
    else:
        return False
    day += 1

print(has_friday13(3,2020))
print(has_friday13(10,2017))
print(has_friday13(1,1985))
print(has_friday13(5,2000))
'''
Nathan Crowley - 14/7/2020

function to convert dates from MM/DD/YYYY format to YYYYDDMM.
'''

def convert_dumb_american_dates(date):
    temp = date.split('/')
    converted_date =''
    reversed_temp = temp[::-1]
    for number in reversed_temp:
        converted_date+=number
    return '{} --> {}.'.format(date,converted_date)

print("\nMM/DD/YYYY --> YYYYDDMM\n",("-"*20))
print(convert_dumb_american_dates("11/12/2019"))
print(convert_dumb_american_dates("12/31/2019"))
print(convert_dumb_american_dates('07/14/2020'))
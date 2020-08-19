'''
3/7/2020
            WORKING.
'''

def How_many_Vowels(string):
    vowel_counter = 0
    vowel_list = []
    vowels = 'a e i o u'
    for letter in string:
        if letter in vowels:
            vowel_counter +=1
            vowel_list.append(letter)
    return "There is {} vowels in {}.   vowels_list {}".format(vowel_counter,string,vowel_list)


userString = input("Please enter a string >>> ")
print(How_many_Vowels(userString))
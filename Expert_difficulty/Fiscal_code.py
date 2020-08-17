'''
Nathan Crowley 17/7/2020

Given an object containing the personal data of
        a person object "firstname,surname,gender,DOB(DD/MM/YYYY)
return the 11 code character fiscal code of the entered persons.
I return as a dictionary with names:fiscal_code as the key_value.
'''


'''create the outlines for a person object'''
class Person:
#constructor
    def __init__(self,firstname,surname,gender,DOB):
        self.__fname = firstname
        self.__sname = surname
        self.__gen = gender
        self.__date = DOB

    def __str__(self):
        return '{} {}, {}, {}.'.format(self.get_fname(),self.get_sname(),self.get_gender(),self.get_DOB())
#getters and setters
    def get_fname(self):
        return self.__fname
    def get_sname(self):
        return self.__sname
    def get_gender(self):
        return self.__gen.upper()
    def get_DOB(self):
        return self.__date
    def get_fullname(self):
        return self.__fname+' '+self.__sname

def generate_fiscal_code(person):
    Sur_cap_letters = ''
    Fname_cap_letters = ''
    letters_and_numbers = ''
    fiscal_code = ''
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    consonants_count = 0
    vowels_count = 0
    sname_consonants = []
    sname_vowels = []
    '''generate 3 capital letters from surname'''
#count number of consonants in surname
    for letter in person.get_sname():
        if letter.lower() in consonants:
            sname_consonants.append(letter)
            consonants_count+=1
        elif letter.lower() in vowels:
            sname_vowels.append(letter)
            vowels_count+=1
#if at least 3 consonantas use the first 3
    if consonants_count >= 3:
        for l in sname_consonants[:3]:
            Sur_cap_letters+=l
#if less than 3 then vowels but at least 3 letters replace empty spot in same order as they appear
    elif (consonants_count < 3) and len(person.get_sname())>=3:
        for con in sname_consonants:
            Sur_cap_letters+=con
        for vow in sname_vowels:
            Sur_cap_letters+=vow
#if less than three letters then fill empty spots with 'X'
    elif len(person.get_sname()) < 3:
        for letter in person.get_sname():
            Sur_cap_letters+=letter
        Sur_cap_letters+='x'
#return Sur_cap_letters[:3].upper()
#print(Sur_cap_letters[:3].upper())
    fiscal_code+=Sur_cap_letters[:3].upper()    #add the first 3 letters to the fiscal code
#generate 3 capital letters from firstname
    consonants_count = 0                    #reset the counters
    vowels_count = 0
    fname_consonants = []
    fname_vowels = []
    for letter in person.get_fname():
        if letter.lower() in consonants:
            fname_consonants.append(letter)
            consonants_count += 1
        elif letter.lower() in vowels:
            fname_vowels.append(letter)
            vowels_count += 1
#exactly 3 consonants use these
    if consonants_count == 3:
        for l in fname_consonants[:3]:
            Fname_cap_letters+=l
#more than 3 use [0],[2],[3]
    elif consonants_count > 3:
        Fname_cap_letters+= fname_consonants[0]
        Fname_cap_letters += fname_consonants[2]
        Fname_cap_letters += fname_consonants[3]
#less than 3 consonants then replace spots with vowels
    elif (consonants_count < 3) and len(person.get_fname())>=3:
        for con in fname_consonants:
            Fname_cap_letters+=con
        for vow in fname_vowels:
            Fname_cap_letters+=vow
#if less than 3 letters then replace with 'X'
    elif len(person.get_fname()) < 3:
        for letter in person.get_fname():
            Fname_cap_letters+=letter
        Fname_cap_letters+='x'
#print(Fname_cap_letters[:3].upper())
    fiscal_code+=Fname_cap_letters[:3].upper()                  #add to fiscal code
#generate 2 numbers, 1 letter , 2 numbers from DOB and gender
    '''(2 numbers)take last two digits of DOB year'''
    date = person.get_DOB()
    date = date.split('/')
    year = date[-1]
#add the two digits
    letters_and_numbers+=year[2::]
    '''(1 letter)generate letter corresponding to month'''
    months = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "H",7: "L", 8: "M", 9: "P", 10: "R", 11: "S", 12: "T"}
    month = int(date[1])        #convert to int as it was a string and cant check string in dict
    if month > 12 or month < 1:
        return ValueError           #error check
#add the letter
    letters_and_numbers+=months[month]
    '''(2 numbers) males = if day less than 10 put '0' infront
                femals = add 40 to the day'''
    day = int(date[0])
    if person.get_gender() == 'M':
        if day < 10:
            letters_and_numbers += '0'+str(day)
        else:
            letters_and_numbers += str(day)
    elif person.get_gender() == 'F':
        day += 40
        letters_and_numbers += str(day)
    else:
        return ValueError
#add these numbers and letter to the fiscal code
    fiscal_code+=letters_and_numbers
#return string fiscal code
    return fiscal_code

'''------------------------------Test Code------------------------------
'nathan crowley M 23/05/2000'

To test correctly, 
    - run the program
    - enter the first person you want to create - Create a person object "firstname,surname,gender,DOB(DD/MM/YYYY)
    - you will be asked if you would like to continue? (Y/N)
    - when completed the program will return a dictionary of people and their fiscal codes
    
'''
#create people objects
list_of_people = {}
user_input = input('Create a person object "firstname,surname,gender,DOB(DD/MM/YYYY)" [ENTER to exit]>>>')
while user_input != '':
    user_input = user_input.split()
    # create person object
    person = Person('{}'.format(user_input[0]), '{}'.format(user_input[1]), '{}'.format(user_input[2]),'{}'.format(user_input[3]))
    # generate their fiscal code
    list_of_people[person.get_fullname()] = generate_fiscal_code(person)
    user_input = input('Create another person object(firstname,surname,gender,DOB) [ENTER to exit]>>>')
print(list_of_people)

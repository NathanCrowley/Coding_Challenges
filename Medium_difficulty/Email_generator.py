class Employee:
    def __init__(self,first,second):
        self.first = first
        self.second = second

    def email(self):
        email = self.first.lower() + '.' + self.second.lower() + '@company.com'
        return email

    def fullname(self):
        fullname = self.first + ' ' + self.second
        return fullname

    def firstname(self):
        return self.first
    def secondname(self):
        return self.second

#-----------------------------------Create instances of Employee object--------
emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")
#--------------------------------------TEST----------------------------------
print(emp_1.fullname())
print(emp_2.email())
print(emp_3.firstname())


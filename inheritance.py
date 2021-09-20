# Py Practice
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

        def fullname(self):
            print(self.fname + ' ' + self.lname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def declare(self):
        print(self.fname, self.lname,
              "is part of the Class of", self.graduationyear)


person = Student('Stacey', 'Wilson', 2019)

person.declare()

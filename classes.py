# Py Practice


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name +
              " and I am " + self.age + " years old!")


person = Person('Stacey', str(50))

# override age in self.age in person
person.age = str(49)

person.myfunc()

#Sometimes you might want to add some extra behavior whan you access or change a property
#A getter is a method that is use to get the value of a property
#A setter is a method that is use to set the value of a property.

class Dog:
    def __init__(self, name, breed, age):
        self.__age = age
        #actual age of the dog is stored in a private variable

    @property
    def age(self):
        return self.__age
        #this is the getter method

    @age.setter
    def age(self, value):
        self.__age = max(0, value)
        #this is the setter method, which makes sure the age is always at least 0


dog1 = Dog("Fido", "labrador", 3)
print(dog1.age)
dog1.age = -4 
print(dog1.age)
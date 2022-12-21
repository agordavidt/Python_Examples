class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

def main():
    #create an instance/object of the Class Dog
    dog1 = Dog("Fido", "labrador", 3)
    print(dog1.name)
    print(dog1.breed)
    print(dog1.age)
main()

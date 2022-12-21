class Dog:
    #the init method is called to create an object
    #we give default values for the fields if none are provided
    
    def __init__(self, name="", height=0, weight=0):
        #self allows an object to refer to itself
        #it is like how you refer to yourself with my

        #we will take the values passed in and assign
        #them to the new dog objects fields (attributes)
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print(f"the name of the dog is {self.name}")
    def eat(self):
        print(f"{self.name} is {self.height} tall")
    def bark(self):
        print(f"{self.name} the dog barks")

def main():
    #create a dog object
    spot = Dog("Spot", 66, 26)
    spot.bark()
    spot.run()
    spot.eat()
main()
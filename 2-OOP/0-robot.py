# Encapsulation is often accomplished by providing two kinds of methods for attributes.
class Robot:
    def __init__(self, name=None):
        self.name = name
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
    def set_name(self, name):
        self.name = name
    def get__name(self):
        return self.name

x = Robot()
x.set_name("Natoshi")
print(x.get__name())
x.say_hi()
y = Robot()
y.set_name(x.get__name())
print(y.get__name())
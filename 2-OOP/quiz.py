class User:
    pass


u = User()

u.name = "John"
u.state = "lagos"
u.year = 2023
print(u.__dict__) #dict stores the attributes and their corresponding values.
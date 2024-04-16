class Friend :

    # class attribute
    name = " "
    age = 0
    weight = 1

# create friend1 object
Friend1 = Friend()
Friend1.name = "TAMMY"
Friend1.age = 19
Friend1.weight = 45

# create another object Friend2 
Friend2 = Friend()
Friend2.name = "AMMY"
Friend2.age = 18
Friend2.weight = 55

# access attributes
print(f"{Friend1.name} is {Friend1.age} years old has {Friend1.weight} wieght ")
print(f"{Friend2.name} is {Friend2.age} years old has {Friend2.weight} wieght ")
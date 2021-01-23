class Dog():

    #   CLASS OBJECT ATTRIBUTE
    species = "Mammal"

    #   METHODS INSIDE OF A CLASS
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

mydog = Dog("Labrador","Tommie") #      OR           mydog = Dog(breed="Labrador",name="Tommie")
print(mydog.breed)
print(mydog.name)
print(mydog.species)

# ------------------------------------------------------------------------------

class Circle():

    pi = 3.14

    def __init__(self,radius = 1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

myc = Circle(3)
print(myc.area())
print(myc.radius)

#   Changing attributes of a class ---------------------------------------------

class Circle():

    pi = 3.14

    def __init__(self,radius = 1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self,new_r):
        self.radius = new_r

myc = Circle(3)
myc.set_radius(738)
print(myc.area())
print(myc.radius)

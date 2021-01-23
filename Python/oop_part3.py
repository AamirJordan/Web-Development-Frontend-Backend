#   INHERITANCE ----------------------------------------------------------------(Creating a class{derived class} within a class{base class})
class Animal():

    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("eating")


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")


    def bark(self):
        print("bhow")

    def eat(self):
        print("dog eating")             #   Over-writes the previous attribute in a new class

mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()


#   SPECIAL METHODS ------------------------------------------------------------
class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages


    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title,self.author,self.pages)

b = Book("Python","Aamir",300)
print(b)

# ------------------------------------------------------------------------------
class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages


    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title,self.author,self.pages)

    def __len__(self):
        return self.pages

b = Book("Python","Aamir",300)
print(len(b))

# ------------------------------------------------------------------------------

class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages


    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title,self.author,self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book was destroyed!")


b = Book("Python","Aamir",300)
del b

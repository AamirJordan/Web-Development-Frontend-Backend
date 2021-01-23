#   Global And Local Variables ------------------------------------------------
x = 25                                          # (GLOBAL VARIABLE)

def my_func():
    x = 50                                      # (LOCAL VARIABLE)
    return x

print(x)






x = 25

def my_func():
    x = 50
    return x


print(x)
print(my_func())







x = 25

def my_func():
    x = 50
    return x


my_func()
print(x)






x = 50

def func(x):
    print("x is:", x)
    x = 1000
    print("x is changed to:", x)

func(x)
print(x)

#   Changing Global variable Locally -------------------------------------------
x = 50

def func():
    global x
    x = 1000
    return x

print("before function call, x is:", x)
x = func()
print("after function call, x is:", x)
#   Lambda Expressions ---------------------------------------------------------

#   Local ----
#lambda x = x**2

#   Enclosing function locals ----
name = "This is a global name!"

def greet():
    name = "Aamir"

    def hello():
        print("Hello " + name)

    hello()
greet()

# ------- OR --------
name = "This is a global name!"                 # (GLOBAL VARIABLE)

def greet():
    #name = "Aamir"                             # (LOCAL VARIABLE)

    def hello():
        print("Hello " + name)

    hello()
greet()

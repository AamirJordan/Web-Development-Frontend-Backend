#   Functions ------------------------------------------------------------------
def my_func(param1 = "default"):
    print("my first python funtion!")

my_func()



def hello():
    print("hello")

hello()



def hello():
    return "hello"

result = hello()
print(result)



def addNum(Num1,Num2):
    if type(Num1) == type(Num2) == type(1):
        return (Num1 + Num2)
    else:
        return "Sorry! Please provide an integer"

result = addNum(70, 47)
print(result)

#   Lamda Expressions ----------------------------------------------------------

# -------- Filter --------
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2==0

evens = filter(even_bool,mylist)
print(list(evens))



# -------- Land Function --------
mylist = [1,2,3,4,5,6,7,8]

lambda num:num%2==0

evens = filter(lambda num:num%2==0,mylist)
print(list(evens))



#   Useful methods of split and in ---------------------------------------------

tweet = "Go sports! #Sports"
result = tweet.split("#")
print(result)


tweet = "Go sports! #Sports"
result = tweet.split("#")[1]
print(result)



print("x" in [1,2,3])
print("x" in [1,2,3, "x"])

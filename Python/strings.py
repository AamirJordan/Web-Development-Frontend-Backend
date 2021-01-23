#   Basics ---------------------------------------------------------------------
'hello'
"hello"
"I'm a dog"

mystring = "abcdefg"
print(mystring)

mystring = "abcdefg"
print(mystring[3])

#   Slicing --------------------------------------------------------------------
mystring = "abcdefg"
print(mystring[3:])

mystring = "abcdefg"
print(mystring[:3])

mystring = "abcdefg"
print(mystring[2:5])

mystring = "abcdefg"
print(mystring[:]) #-------**Returns the entire string**-------#

mystring = "abcdefg"
print(mystring[::1]) #-------**Returns every following element in a string**-------#

mystring = "abcdefg"
print(mystring[::2]) #-------**Returns skipped element in a string**-------#





#   Basic Methods --------------------------------------------------------------

mystring = "abcdefg"
x = mystring.upper()
print(x)

y = mystring.lower()
print(y)

z = mystring.capitalize()
print(z)

my_name = "Aamir Sohail Farooqui"
s = my_name.split("a")
print(s)    #---------- Splits string from that element. Or words if left blank----------#




#   Print Formatting -----------------------------------------------------------

a = "Insert another string here: {}".format("INSERT ME!")
print(a)


#   b = "Item One: {} Item Two: {}".format("dog","cat")
#   print(b)
#-------------------  OR -------------------------#
b = "Item One: {y} Item Two: {x}".format(x="Dog",y="Cat")
print(b)

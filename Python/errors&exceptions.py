try:
    e = open("errors&exceptions.txt","w")
    e.write("Write here")
except:
    print("Error! Could not find file or write data")
else:
    print("SUCCESS!")

    e.close()

print("hello world!")

#   ----------------------------------------------------------------------------

try:
    e = open("errors&exceptions.txt","r")
    e.write("Write here")
except:
    print("Error! Could not find file or write data")
else:
    print("SUCCESS!")

    e.close()

print("hello world!")

#   ----------------------------------------------------------------------------

try:
    e = open("errors&exceptions.txt","w")
    e.write("Write here")
except:
    print("Error! Could not find file or write data")
else:
    print("SUCCESS!")
finally:
    print("I always work no matter what")

    e.close()

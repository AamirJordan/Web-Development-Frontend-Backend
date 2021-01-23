#   IF ELSE --------------------------------------------------------------------
if 1<2:
    print("yes!")
    if 2<3:
        print("yes!!")


if 1<2:
    print("First Block")
    if 20<3:
        print("Second Block")


if 1<2:
    print("hello")
else:
    print("last")



if 1>2:
    print("hello")
else:
    print("last")


if 1 == 1:
    if 1>2:
        print("hello")
    elif 3 == 3:
        print("elif ran")
    else:
        print("last")


#    FOR loop ------------------------------------------------------------------

seq = [1,2,3,4,5,6]

for item in seq:
    #code here
    print(item)



seq = [1,2,3,4,5,6]

for item in seq:
    #code here
    print("hello")



d = {"Sam":1, "Frank":2, "Dan":3}

for item in d:
    print(item)


d = {"Sam":1, "Frank":2, "Dan":3}

for k in d:
    print(k)
    print(d[k])





#   Tuple and Packing ----------------------------------------------------------
mypairs = [(1,2),(3,4),(5,6)]

for item in mypairs:
    print(item)



mypairs = [(1,2),(3,4),(5,6)]

for tup1,tup2 in mypairs:
    print(tup1)
    print(tup2)



mypairs = [(1,2),(3,4),(5,6)]

for tup1,tup2 in mypairs:
    print(tup2)
    print(tup1)




#   While Loop -----------------------------------------------------------------
i = 1

while i < 5:
    print("i is: {}".format(i))
    i+=1




#   Range ----------------------------------------------------------------------
for item in range(10):
    print(item)


#   List Comprehension ---------------------------------------------------------
x = [1,2,3,4]

out = []
for num in x:
    out.append(num**2)
print(out)

#------- OR --------

out = [num**2 for num in x]
print(out)

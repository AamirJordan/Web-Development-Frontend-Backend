mylist = [1,2,3]
print(mylist)

mylist = [1,2,3]
print(len(mylist))

mylist = ['a','b','c','d','e','f','g']
print(mylist[0])

mylist = ['a','b','c','d','e','f','g']
print(mylist[-1])

mylist = ['a','b','c','d','e','f','g']
print(mylist[1:])

mylist = ['a','b','c','d','e','f','g']
print(mylist[1:5])



#   Lists are mutable ----------------------------------------------------------
mylist = ['a','b','c','d','e','f','g']
print("before reassignment")
print(mylist)

mylist[0] = "New Item"
print("after reassignment")
print(mylist)



#   Append ---------------------------------------------------------------------
mylist = ['a','b','c','d','e','f','g']
mylist.append(["x","y","z"])
print(mylist)



#   Extend ---------------------------------------------------------------------
mylist = ['a','b','c','d','e','f','g']
mylisttwo = ['x','y','z']
mylist.extend(mylisttwo)
print(mylist)



#   Pop ------------------------------------------------------------------------
mylist = ['a','b','c','d','e','f','g']
item = mylist.pop(3)
print(mylist)
print(item)



#   Reverse --------------------------------------------------------------------
mylist = ['a','b','c','d','e','f','g']
mylist.reverse()
print(mylist)



#   Sort -----------------------------------------------------------------------
mylist = [7,3,97,100,56,1,9,44,83]
mylist.sort()
print(mylist)



#   Nested Lists ---------------------------------------------------------------
mylist = [1,2,['x','y','z']]
print(mylist[2][1])



#    List Comprehension --------------------------------------------------------
matrix = [[1,2,3],[4,5,6],[7,8,9]]

first_col = [row[0] for row in matrix]
print(first_col)

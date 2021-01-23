# Python C++ program to sort an array of 0s
# 1s and 2s.
import math

def sort012(arr, n):

    # Variables to maintain the count of 0's,
    # 1's and 2's in the array
    count0 = 0
    count1 = 0
    count2 = 0
    for i in range(0,n):
        if (arr[i] == 0):
            count0=count0+1
        if (arr[i] == 1):
            count1=count1+1
        if (arr[i] == 2):
            count2=count2+1


    # Putting the 0's in the array in starting.
    for i in range(0,count0):
        arr[i] = 0

    # Putting the 1's in the array after the 0's.
    for i in range( count0, (count0 + count1)) :
        arr[i] = 1

    # Putting the 2's in the array after the 1's
    for i in range((count0 + count1),n) :
        arr[i] = 2

    return


# Prints the array
def printArray( arr,  n):

    for i in range(0,n):
        print( arr[i] , end=" ")
    print()


# Driver code
arr = [ 0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1 ]
n = len(arr)
sort012(arr, n)
printArray(arr, n) 

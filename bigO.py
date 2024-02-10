# ********n BIG O *****
# Big O is the metric for measuring the efficiency of an algorithm,
# Big O helps in developing efficient algorithms

# Time complexity is a function that describes how long an algorithm
# takes in terms of the quantity of input it receives. Space complexity
# is a function that describes how much memory (space) an algorithm
# requires to the quantity of input to the method.

# In big O, these three symbols are used to represent scenarios for
# performance of an algorithm. But usually we measure the worse case
# 1. Best case     ---- Omega
# 2. Average Case  ---- Big Herta
# 3. Worse Case    ---- Big O

# ************ RUNTIME COMPLEXITIES ********************
# O(1)    -------->  Constant time: eecution time does not change
# eg. Below the number of operations remains the same regardless of
# the value passed to the function
def multiply(n):
    return (n * n)


# print(multiply(2))
# O(n)    -------->  Linear time: execution time changes as the input grow
# Below,  the number of operations will grow proportional to the
# value passed to the function
def print_items(n):
    for i in range(n):
        print(i, end="")


# print_items(4)
# O(logn) -------->  Logrithmic time:
# O(n**2) -------->  Quadratic time
# O(n**2) -------->  Exponential Time


# ******** DROPPING THE CONSTANT *****
def print_items_two(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


# With the above function, the time complexity is O(2n)
# That's becuase O(n) apearing twice ie. 2 x O(n) = O(2n)
# With this we can drop the constant which is 2 so that leaves
# us with a time complexity of O(n)
# print_items_two(5)


# ***** O(n**2) ***********
# Below is what constitutes O(n**2)
# This means for each loop with i, we'll run loop j until i loop
# is done executing. This means j will as many times as i
# which ===> O(n**2)
def print_n_square(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


# print_n_square(5)


# ***** O(n**3) ***********
# In time complexity, this is also
# written as O(n**2)
def print_n_cube(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)


# print_n_cube(3)

# *************** NONE DOMINANT TERMS *******************
# The time complexity for below is O(n**2 + n), with this,
# We remove the non dominant term which n and simplify the
# time compexity to be O(n**2)
def non_dominant(n):
    for i in range(n):
        for j in range(n):
            print(i, j) # O(n**2)

    for k in range(n):
        print(n) # O(n)


# ************ BIG O(logn) ***************************
# This can also be called divide and conquer
# Where you divide the list into to and compare if the item
# you're esarching is larger or smaller than items on the left or right
# With that, git rid of one half depending oon the answer and search the
# half till you find it
# mostly used in binary search algorithm  and quite efficient
# eg.
# log2**8 = 3
# log2**1,048,576 = 20

# ********** SPACE COMPLEXITY *********************
# Results of recursive calls are saved in the stack memory
# Space cpmplexity of recursive calls is O(n)
def sum(n):
    if n <= 0:
        return 0
    return n + sum(n-1)


# print(sum(3))

# Space complexity of the function below is O(1)
def pair_sum_sequence(n):
    total = 0
    for i in range(n):
        total = total + pair_sum(i, i+1)
    return total


def pair_sum(a, b):
    return a + b


# print(pair_sum_sequence(3))

# *********************************************************
# *** DIFFERENT TERMS OF INPUT, ADD VS MULTIPLY ***********
# The time complexity for below is
# O(n+n) = O(2n)
# now we drop the constant which is 2 and simplify if as below
# O(n)
def print_terms(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

# The time complexity for below will be different from above
# due to the input to the function
def print_terms_two(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

# since there are two different input to the function,
# the time complexity for the this is not O(n)
# loop 1 time complexity   ===> O(a)
# loop 2 time complexity   ===> O(b)
# Time complexity for both ===> O(a + b)

def print_terms_two(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)

# Now for nested loop like above,
# Time complexity for nested loop ===> O(a * b)


# ****************************************************
# ********* HOW TO MEASURE CODE USING BIG 0 **********

# Time complexity for the function is O(n)
def find_biggest_num(sample_array):
    biggest_num = sample_array[0] #--------> O(1)
    for index in range(1, len(sample_array)): #-----> O(n)
        if sample_array[index] > biggest_num: #-----> O(1)
            biggest_num = sample_array[index] #-----> O(1)

    print(biggest_num) #----> O(1)


# find_biggest_num([1, 5, 19, -4, 20])


# ****************************************************
# ********* HOW TO MEASURE CODE USING BIG 0 **********
# Arrays are not native data structures in python,
# There are modules for creating arrays of a specific data type
# maily of numeric data type
# Arrays in python can only store elements of same data type
# Modules we can use to create arrays in python are :
# 1. Array module
# 2. Numpy module
# These modules provides arrays data structure that is more memory efficient
# than a list for specific data structures, they store objects contiguous without
# pointers to remove overheads, array objects can only store objects of same data types
# ie. an of integers can not store double or string or any data type

# ***** Types of arrays *******
# 1. One dimesional arrays
myarray = [1,2,3,4,5,56,6]
print(myarray[1])
# 2. Multi dimensional arrays {two dimensional, three dimensional etc.}
my_matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,12,11,12]
]

print(my_matrix[0][2])

# ****** ACCESSING ELEMENTS IN A THREE
# DIMENSIONAL ARRAY *****
# [depth][row][column]
three_dim = [
    [
    [1,2,3,4],
    [5,6,7,8],
    [9,12,11,12]
    ],
    [
    [1,2,3,4],
    [5,6,7,8],
    [9,12,11,19]
    ]
]
# print("Three dimensional: ", three_dim[0][1][0])
# print("Three dimensional: ", three_dim[1][2][3])

# ****************** CREATING ARRAYS IN PYTHON ***************
# Arrays can be created using either  numpuy or array module
# 1. Creating array using array module
import array as ar

miarray = ar.array('i') #-------> time O(1) | space O(1)
my_ar = ar.array('i', [1,2,3,4]) #-------> Time O(nj)| space O(n)
# print("Array module: ", my_ar)

# 2. Creating an array using the numpy module
import numpy as np
np_array = np.array([], dtype=int) #---------> Time  O(1) | space O(1)
np_array2 = np.array([12, 13, 14]) # --------> Time O(n) | spcae O(n)
# print("Numpy Module: ", np_array2)


# ************************************************************
# ***** INSERTING ITEMS IN AN ARRAY USING THE ARRAY MODULE ***
# Inserting into an array, Time complexity O(n)
# Inserting into an array, Space complexity O(1), specific space needed for that element to insert
my_ar.insert(0, 99)
print(my_ar)

# Array traversal means visiting all elements in an array to the end
# This can be achieved using a loop

# Time complexity ---> O(n)
# Space complexity ---> O(1)
def traverser(arr):
    for index in range(len(arr)): #---------> O(n)
        print(arr[index], end=",") #--------> O(1)

# Time complexity ---> O(n)
# Space complexity ---> O(1)
# def traverse_array(array):
#     for i in array: #---------> O(n)
#         print(i) #--------> O(1)

# traverser(my_ar)
# traverse_array(my_ar)

# ******* Accessing an object inside an array ********
# This can be achieved using index
# print("By index: ", myarray[0])

# Time  O(1)
# Space O(1)
def access_array_element(array, index):
    if index >= len(array): #---------> Time O(1) | Space O(2)
        print("No element with the given index exist") #Time O(1) | Space O(2)
    else:
        # print(array[index], index)
        print(array[index]) #-------> Time O(1) | Space O(1)


# access_array_element(myarray)


# *****************************************************
# ********* SEARCHING FOR AN ELEMENT IN AN ARRAY ******
# This can be done using either
# 1. ****** Linear search
# Time O(n)
# Space O(1)
def linear_search(array, target):
    for i in range(len(array)): #------> O(n)
        if array[i] == target: #-------> O(1)
            return i # ---> O(1)
    return -1

print(linear_search([1,2,3,4,5], 9))

# 2. ****** Binary search *********
# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return -1
# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10
# Function call
result = binary_search(arr, 0, len(arr)-1, x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


# ************ DELETING AN ELEMENT FRON AN ARRAY *******
# Removing an element from an element is memory intensive,
# especially when the item is removed from any other place apart from
# from the end, this is becuase all element will need to shift to the
# left to occupy the empty spaces, so the more the elements, the memory
# intensive it will be
# Removing from any other place: Time complexity O(n)
# Removing item from the end: Time O(1)
# Space complexity O(1)
# my_ar.remove(3)
# Worse case overall for deleting an item: O(n)

# **********************************************************
# ********** ONE DIMENSIONAL ARRAY PRACTICE ****************
from array import *
# 1. Create an array and traverse
# Time complexity O(n)
my_array = array('i', [1,2,3,4,5])
for i in my_array:
    print(i)

# 2. Access individual elements though index
# Space O(1)
print(my_array[0])

# 3. Add an element to an array using the append method
# Time complexity O(1)
# Space O(1)
my_array.append(100)
print(my_array)

# 4.Add an element to an array using insert
# Insert takes two values, index and value
# Time complexity O(n)
# Space complexity O(1)
my_array.insert(1, 22)
print(my_array)


# 5. Extend array using extend method
# takes an interable
# my_array.extend((15, 29))
my_array.extend([15, 29])
print(my_array)

# 6. Adding element to array from list
temp_list = [11, 40, 23, 17]
my_array.fromlist(temp_list)
print(my_array)

# remove an array element using remove method
my_array.remove(40)
print(my_array)
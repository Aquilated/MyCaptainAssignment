# 1- List functions from w3schools (any 5)
"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
"""

# 2- String functions from w3schools (any 5)
"""
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
"""

# 3- Dictionary functions from w3schools (any 5)
"""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
"""

# 4- Make a pattern

rows = 5
i = 0
while i <= rows - 1:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = rows - 1
while i >= 0:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1

# 5- Create a Calculator

print("1. Add")
print("2. Multiply")

f = int(input("Select the function you want to execute: "))

while f >= 3:
    print("Please select a valid option")
    f = int(input("Select the action you want to execute: "))

n = input("Enter the numbers you want to equate spaced apart: ")
n = n.split()
numbers = [int(i) for i in n]
total = 0

if f == 1:
    for ele in range(0, len(numbers)):
        total = total + numbers[ele]
    print("Your answer is:", total)
elif f == 2:
    for ele in range(0, len(numbers)):
        total = numbers[ele] * numbers[ele]
    print("Your answer is:", total)

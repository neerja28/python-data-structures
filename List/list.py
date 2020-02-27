# Lists
# Algorithms - A set of rules or steps used to solve a problem
# Data Structures - A particular way of organizing data in a computer

# A list is a kind of collection# A collection allows us to put many values in a single "variable"
# A collection is nice because we can carry many values around in one convenient package
friends = ['Neerja', 'Rooney', 'Lucky', 'Mickey', 'Mini']

# [ ]  is a list constant
# List constants are surrounded by square brackets and the elements in the list are separated by commas
# A list element can be any python object - even another list
# A list can be empty

print(['Neerja', 'Rooney', 'Lucky', 'Mickey', 'Mini'])
>>> ['Neerja', 'Rooney', 'Lucky', 'Mickey', 'Mini']

print([])
>>> []

# Lists and Loops
friends = ['Neerja', 'Rooney', 'Lucky', 'Mickey', 'Mini']
for friend in friends:
    print("Hello", friend)
print("Done!")
#Hello Neerja
#Hello Rooney
#Hello Lucky
#Hello Mickey
#Hello Mini
#Done!

# Looking inside lists
# Just like strings, we can get at any single element in a list using an index specificed in square brackets
friends = ['Neerja', 'Rooney', 'Lucky', 'Mickey', 'Mini']
print(friends[0]) #Neerja

# Lists are mutable
# Strings are immutable - we cannot change the contents of a string - we must make a new string  to make any Change
# Lists are mutable - we can change an element of a list using the index operator
fruit = 'Banana'
fruit[0] = 'b' # Traceback error 'str' object does not support item Assignment

fruit = ['banana', 'mango']
fruit[0] = 'orange'
print(fruit) # ['orange', 'mango']

# length of a List
# The len() function takes alist as a parameter and returns the number of elements in the lists
# len() tells the number of elements of any set or sequence (such as a string...)

greet = 'Hello Bob'
print(len(greet)) # 9
x = [1, 2, 'joe', 99]
print(len(x)) # 4

# Using the range function
# The range function returns a list of numbers that range from zero to one less than the parameter
# We can construct an index loop using for and an integer iterator
print(range(4)) # [0,1,2,3]
friends = ['Neerja', 'Rooney', 'Lucky', 'Mickey', 'Mini']

print(len(friends)) # 5
print(range(len(friends))) # [0,1,2,3,4]

friends = ['Neerja', 'Rooney', 'Lucky', 'Mickey', 'Mini']
for friend in range(len(friends)):
    print('Hello', friends[friend])
# Hello Neerja
#Hello Rooney
#Hello Lucky
#Hello Mickey
#Hello Mini

friends = ['Neerja', 'Rooney', 'Lucky', 'Mickey', 'Mini']
for friend in range(len(friends)):
    print('Hello', friend)
#Hello 0
#Hello 1
#Hello 2
#Hello 3
#Hello 4

# Concatenating Lists using +
# We can create a new list by adding two exisiting lists together
a = [1, 2, 3]
b = [5, 6, 7]
c = a + b
print (c) # [1, 2, 3, 4, 5, 6]
print(a) # [1, 2, 3]

# Lists can be sliced using : operator
# Just like in strings, the second number is "upto but not including"
t = [9, 41, 12, 3, 74, 15]
>>> t[1:3] # [41, 12]
>>> t[:4] # [9, 41, 12, 3]
>>> t[3:] # [3, 74, 15]
>>> t[:] # [9, 41, 12, 3, 74, 15]

# List Methods
x = list()
dir(x)
#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# Building a list from scratch
# We can create an empty list and then add elements using the append method
# The list stays in order and the append method
# The list stays in order and new elemets are added at the end of the list
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff) # ['book', 99]


# Is something in a list
# Python provides two operators that let you check if an item is in a lists
# these are logical operators that return True or False
# they do not modify the list
some = [1, 9, 21, 10, 16]
if 9 in some:
    print('True')
if 20 not in some:
    print("True")

# Lists are in Order
# A list can hold many items and keeps those items in the order until we do something to change the order
# A list can be sorted
friends = ['Neerja', 'rooney', 'Lucky', 'mickey', 'Mini']
friends.sort()
print(friends) # ['Lucky', 'Mini', 'Neerja', 'mickey', 'rooney']

# Built-in Functions and Lists
# There are a number of functions built into python that takes lists as parameter
nums = [3, 41, 12, 9, 74, 15]
len(nums) # 6
max(nums) # 74
min(nums) # 3
sum(nums) # 154
print(sum(nums)/len(nums)) # 25.6

#files program using lists
numlist = list()
while True:
    inp = input("Enter a number:")
    if inp =='done' : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print("Average:, average")

# Strings and lists
# Split() Method
# Split breaks a string into parts and produces a list of strings.
# We think of these as words.
# We can access a particular word or loop through all the words 

lst = "Hello my name is Neerja"
res = lst.split()
print(res) # ['Hello', 'my', 'name', 'is', 'Neerja']
print(len(res)) # 5
print(res[0]) # Hello
# Looping through a list
for words in res:
    print(words)
# Hello
# my
# name
# is
# Neerja

# Spilt() method uses space as the default demiliter
# When you do not specify a delimiter , multiple spaces are treated like one delimiter
# You can specify what delimiter character to use in the splitting
#Ex1:
line = "A lot              of spaces"
res = line.split()
print(res) # ['A', 'lot', 'of', 'spaces']

#Ex2:
line = "first;second;third"
res = line.split()
print(res) # first;second;third

#Ex3:
line = "first;second;third"
res = line.split(';')
print(res) # ['first', 'second', 'third']

# Extracting variables using split function

# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008




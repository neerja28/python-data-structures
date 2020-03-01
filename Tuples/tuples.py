#tuples
# tuples are unmodifiable Lists
# Tuples are another kind of sequence that functions much like a list
# They have elements which are indexed starting at 0

# Tuples are like lists
x = ('Glenn', 'Sally', 'Joseph')
print(x[2]) #Joseph

y = (1, 9, 2)
print(y) # (1, 9, 2)
print(max(y)) #9

for iter in y:
    print(iter)
# 1
# 9
# 2

# Tuples are immutable
# Unlike a list once you create a tuple you cannot either alter its contents (similiar to a string)
# Srings are tuples are immutable

#Lists
a = {9,7,4}
a[2] = 5
print(a) #{9,7,5}
#Strings
y = 'ABC'
y[2] = 'D' #Traceback Error
#Tuples
z = (5,4,3)
z[1] = 8
print(z) # Traceback error

# List and Tuple functions
l =list()
print(dir(l))
# 'append', 'clear', 'copy', 'count', 'extend', 'index',
# 'insert', 'pop', 'remove', 'reverse', 'sort'
t = tuple()
print(dir(t))
# 'count', 'index'

# Tuples are more EFFICIENT
# Python does not have to build tuple structures to be modifiable
# They are simpler and more efficient in terms of memory use and performance than lists
# When we are creating "temporary variables" we prefer tuples over Lists
# As you above tuples have less functions, so that the values are not modified. (immutable property)

# Tuples and Assignments
# We can also put a tuple on the left hand side of an assignment statement
# We can even omit the parenthesis
(x, y) = (4, 'fred') # simultaneous assignment statement
print(y) # fred
print(x) # 4

# Tuples and Dictionaries
# The items method in dictionaries returns alis of (key, value) tuples
d = dict()
d['key1'] = 100
d['key2'] = 200
for (k,v) in d.items(): # tuple assignment
    print(k, v)
# key1 100
# key2 200
tupls = d.items()
print(tupls)
# dict_items([('key1', 100), ('key2', 200)])

# Tuples are Comparable
# The comparison operators work with tuples and other sequences. If the first items# is equal, python goes on
# the next element, and so on until it finds elements that differ

>>> (0,1,2) < (5,1,2)
>>> True # doesnt check 1 < 1 and 2 < 2

>>> (0,1,20000) < (0, 3, -4)
>>> True # 0 = 0 moves onto 1 < 3, doesnt check 20000 < -4

>>> ('Jones', 'Sally') < ('Jones', 'Sam')
>>> True # checks Sal < Sam, doesnt check ly

>>>('Jones', 'Sally') > ('Adams', 'Sam')
>>> True # doesnt check Sally > Sam

# Sorting Lists of tuples
# We can take advantage of the ability to sort a list of tuples to get a sorted version of a Dictionary
# First we sort the dictionary by the key using the items() method and sorted() function
# Keys are always unique in a Dictionary
d = {'Neerja': 2, 'rooney': 1, 'Lucky': 1, 'Micky': 1, 'Mini': 1}
print(d.items()) # dict_items([('Neerja', 2), ('rooney', 1), ('Lucky', 1), ('Micky', 1), ('Mini', 1)])
print(sorted(d.items())) # [('Lucky', 1), ('Micky', 1), ('Mini', 1), ('Neerja', 2), ('rooney', 1)]

#Sort by Keys
for k,v in sorted(d.items())
    print(k,v)
#Lucky 1
#Micky 1
#Mini 1
#Neerja 2
#rooney 1

# Sort by Values
# If we could construct a list of tuples of the form (value, key) we could sort the value
# We do this with a for loop that creates a list of tuples

d = {'Neerja': 2, 'rooney': 1, 'Lucky': 1, 'Micky': 1, 'Mini': 1}
l = list()
for k,v in d.items():
    l.append((v,k)) # ((v,k)) cause append takes 1 argument
sort_l = sorted(l)
print(sort_l) # List of 5 tuples
# [(1, 'Lucky'), (1, 'Micky'), (1, 'Mini'), (1, 'rooney'), (2, 'Neerja')]
reverse_sort_l = sorted(l, reverse=True)
print(reverse_sort_l)
# [(2, 'Neerja'), (1, 'rooney'), (1, 'Mini'), (1, 'Micky'), (1, 'Lucky')]




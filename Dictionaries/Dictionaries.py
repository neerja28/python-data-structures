# Dictionaries
# What is a collection?
# A collection is nice because we put more than one value in it and carry them all around in one convivient package
# We have a bunch of values in a single "variable"
# We do this by having more than one place "in" the variable
# We have ways of finding different places in the variable

# Lists and Dictionaries
List : A liner collection of values that stay in order
Dictionary : A bag of values, each with its own value

# Dictionaries
Dictionaries are pythons most powerful data collection
Dictionaries allow us to do fast database-like operations in python
They are memory based key-value stores

# Dictionaries
# lists index their entries based on the position in the list
# Dictionaries  are like bags - no order
# So we index the things we put in the dictionary with a lookup tags

purse = dict()
purse['car_keys'] = 1
purse['badge'] = 2
purse['wallet'] = 3
print(purse) # {'car_keys': 1, 'badge': 2, 'wallet': 3}
print(purse['wallet']) # 3
purse['wallet'] = purse['wallet'] + 2
print(purse) # {'car_keys': 1, 'badge': 2, 'wallet': 5}

# Comparing Lists and Dictionaries
List and Dictionaries are MUTABLE.
Dictionaries are like lists except that they use keys instead of numbers to look up values
List use position to access values.
Dictionaries uses keys to access values.

lst = list()
lst.append(21)
lst.append(183)
print(lst) # [21, 183]
lst[0] = 23
print(lst) # [23, 183]

^^ same using dictionaries
numbers = dict()
numbers['age'] = 21
numbers['year'] = 2020
print(numbers) #{'age': 21, 'year': 2020}
numbers['age'] = 27
print(numbers) # {year': 2020', 'age': 27}

# Dictionary Literals
# Dictionary literals use curly braces and have a list of key : value pairs
# You can make an empty dictionary using empty curly braces
d = {'car_keys': 1, 'badge': 2, 'wallet': 5}
print(d) # {'badge': 2, 'wallet': 5, 'car_keys': 1}
empty_d = {}
print(dic) # {}

# Dictionary Tracebacks
# It is an error to reference a key which is not in the dictionary
# We can use the in operator to see if a key is in the dictionary
d = dict()
print(d['age'])  # traceback error keyError
>>>'age' in d # False


# Example1
counts = dict()
names = ['Neerja', 'rooney', 'Lucky', 'Micky', 'Mini', 'Neerja']
for name in names:
    if name in counts:
        counts[name] = counts[name] + 1
    else:
        counts[name] = 1
print(counts)
# {'Neerja': 2, 'rooney': 1, 'Lucky': 1, 'Micky': 1, 'Mini': 1}

# Example2
# the get method for dictionaries
# the pattern of checking ato see if a key is already in a dictionary and assuming a default value if the key is not there is so comman
# that there is a method called get() that does this for us

# Default value if key does not exist (and no traceback)
counts = dict()
names = ['Neerja', 'rooney', 'Lucky', 'Micky', 'Mini', 'Neerja']
for name in names:
    counts[name] = counts.get(name, 0) + 1 # the default value is zero
print(counts)

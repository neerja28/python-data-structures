# String Data type

# String is a sequence of characters
# A string literal uses quotes 'Hello' or "Hello"
# For Strings, + means "concatenate"
# When a string contains numbers, it is still a string
# We can convert numbers in a string into a number using int()

# String Concatenation
str1 = "Hello"
str2 = "There"
res = str1 + str2
print (res) # HelloThere
res1 = str1 + ' ' + str2
print(res1) # Hello There
str3 = '12345'
res2 = int(str3) + 1
print(res2) # 12346

# Reading and Converting
# We prefer to read data in using strings and then prase and convert the data as we need
# This gives us more control over error situations and/or bad user input
# Input numbers must be converted from strings
num = input("Enter a digit: ")
res3 = int(num) + 10
print(res3)

# Looking inside Strings
# We can get at any single character in a string using an index specified in square brackets
# The index value must be an integer and starts at zero
# The index value can be an expression that is computed
# You will get a python error if you attempt to index beyond the end of a strings (string index out of range)
fruit = "banana"
print(fruit[1]) # a
x = 3
print(fruit[x-3]) # b

# len() function
# Built-in function len gives us the length of a string, ie. takes in a string and outputs a number
fruit = 'banana'
print(len(fruit))

# Looping strings
# A definite loop sing a for statement is much more elegant
# The iteration variable is completely taken care of by the for loop

# while loop
fruit = 'banana'
index = 0
while index < len(fruit):
    print(fruit[index])
    index += 1

# for loop
fruit = "orange"
for index in fruit:
    print(index)

# Looping an Counting
# Count the number of "a"
# The iteration variable "iterates" through the string and the block(body) of code
# is executed once for each value in the sequence
fruit = "banana"
count = 0
for letter in fruit:
    if letter == 'a':
        count += 1
print(count)

# Slicing Strings
# We can look at any continous section of a string using a colon operator
# the second number is one beyond the end of the slice - "upto but not including"
# If the second number is beyond the end of the string, it stops at the end
name = "Neerja Narayanappa"
print(name[0:4]) # Neer
print(name[4:5]) # j
print(name[7:100]) # Narayanappa
print(name[:4]) # Neer
print(name[7:]) # Narayanappa
print(name[:]) # Neerja Narayanappa

# Using in as a logical operator
# The in keyword can also be used to check to see if one string is in another string
# The in expression is a logical expression that returns True or False and can be usd in an if statement
# >>> fruit = 'banana'
# >>> 'n' in fruit:
#True
#>>> 'z' in fruit:
#False
fruit = 'banana'
if 'a' in fruit: # Dont forget quotes for 'a'
    print("Found it!")

# String comparison
# Ascii of Capital letter is lesser than Ascii of small letters
word = input("Enter a word") #Neerja
if word < 'banana':
    print('your word' + word + 'comes before banana') #Gets printed
elif word > 'banana':
    print('your word' + word + 'comes after banana')
else:
    print('your word' + word + 'is same as banana')

# String Library
# lower, upper, caqpitalize, find
name = 'Richard Hendricks'
print (name.lower()) # richard hendricks
print(name.upper()) # RICHARD HENDRICKS
print(name.capitalize()) # Richard hendricks

# We use the find( function to search for a sunstring within another string
# find() finds the first occurrence of the substring
# If the substring is not found, find() returns -1
# Remember the string position starts at 0 always
fruit = 'banana'
position = fruit.find('na')
print(position) # 2
position = fruit.find('z')
print(position) # -1

# Search and Replace
name = "Bangalore, KA"
name_res = name.replace('Bangalore', 'Bengaluru')
print(name_res)

# Striping White Space
msg = "      Hello World     "
print(msg.lstrip()) # "Hello World     "
print(msg.rstrip()) # "      Hello World"
print(msg.strip()) # "Hello World"

# Prefixes
line = "Please open the door"
print(line.startswith('Please')) # True
print(line.startswith('p')) # False

# Parsing and Extrating
data = "From neerja.narayanappa@aa.com Sat Jan 5 9:14:16 2008"
findsymbolindex = data.find('@') # Just go find where @ is
findEndsymbolindex = data.find(' ', findsymbolindex) # search for a space Starting From @
domain_name = data[findsymbolindex+1 : findEndsymbolindex]
print(domain_name) # aa.com

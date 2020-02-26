# Files
# Files are stored in the secondary memory

# Opening a File
# open() function is used to opening a File
# open() returns a file handle - variable used to perform operations on the file
# Syntax
handle = open(filename, mode)
fhand = open(words.txt, 'r')
# Returns a handle used to manipulate the file
# Filename is a string
# Mode is optional, must be r for read and w for Write


# Handle
>>> fhand = open('words.txt')
>>> print(fhand)
<open file 'words.txt', mode 'r' at 0x1006e05d0>
# Throws a traceback if the file is not present
>>> fhand = open('words\.txt')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IOError: [Errno 2] No such file or directory: 'words\\.txt'

# Newline Character
# We use a special character called the 'newline' to indicate whena line ends
# We represent it as \n in String
# Newline is still one character - not two
stuff = "Hello\nWorld"
print(stuff)
# Hello
# World
stuff = 'A\nB'
print(len(stuff)) # 3

# File handle as a sequence
# A file handle open for read can be treated as a sequence of strings
# where each line in the file is a string in the sequence
# We can use the for statement to iterate through a sequence
# A sequence is a ordered set
xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)

# Counting lines in a file
# Open a file read-only
# use a for loop to read each line
# count the lines and print out the number of lines
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print ("Line count:", count)


# Reading the whole file
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20]) # From stephen.marquar

# Searching through the file 
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line startswith('From:'):
        print(line)

#alternate code , skipping with continue
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line startswith('From:'):
        continue
    print(line)

# Using in to select lines
# We can look for a string anywhere in a line as our selection criteria
# Prints all the lines that has uta.edu
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uta.edu' in line:
        continue
    print(line)

# Prompt for a file name
fname = input("Enter a filename:")
fhand = open(fname)
count = 0
for line in fhand:
    if line startswith('Subject'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

# try and exccept block for bad file names
fname = input('Enter the file name:')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()



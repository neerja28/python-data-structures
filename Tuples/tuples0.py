# Find the top ten comman words using tuples
fhand = open("romeo.txt")
counts =  dict()
for line in fhand :
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key,value in counts.items():
    newtuple = (value, key)
    lst.append(newtuple)
print(lst)
# [(1, 'But'), (1, 'soft'), (1, 'what'), (1, 'light'), (1, 'through'), (1, 'yonder'), (1, 'window'), (1, 'breaks'), (1, 'It'), (3, 'is'), (3, 'the'), (1, 'east'), (3, 'and'), (1, 'Juliet'), (2, 'sun'), (1, 'Arise'), (1, 'fair'), (1, 'kill'), (1, 'envious'), (1, 'moon'), (1, 'Who'), (1, 'already'), (1, 'sick'), (1, 'pale'), (1, 'with'), (1, 'grief')]
lst = sorted(lst, reverse=True)
# Print the top 10 most comman words
for value, key in lst[:10]:
    print(key,value)

"""
the 3
is 3
and 3
sun 2
yonder 1
with 1
window 1
what 1
through 1
soft 1

"""

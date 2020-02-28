fname = input("Enter the name of the file")
fh = open(fname)
counts = dict()
for line in fh :
    words = line.split()
    for eachword in words:
        counts[eachword] = counts.get(eachword, 0) + 1
        print(eachword, counts[eachword])
print(counts)

bigcount = None
bigword = None
for k, v in counts.items():
    if bigcount is None or v > bigcount:
        bigword = k
        bigcount = v
print(bigword, bigcount) # is 3




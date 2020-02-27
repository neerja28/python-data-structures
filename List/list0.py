fname ="romeo.txt"
fh = open(fname)
lst = list()
for line in fh:
    sentence = line.rstrip().split()
    # You handle one line at a time, dont comvert all the lines all at once.
    for word in sentence:
        if word in lst:
            continue
        else:
            lst.append(word)
lst.sort()
print(lst)
print(sentence)

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
d = {}
for line in fh:
    if line.startswith("From "):
        line.rstrip()
        words = line.split()
        hour = words[5].split(":")
        d[hour[0]] = d.get(hour[0],0) + 1

lst = []
for k,v in d.items():
    lst.append((k,v))
lst.sort()
for k,v in lst:
    print (k,v)

fname = "mbox-short.txt"
fh = open(fname)
lst = []
counts = {}
for line in fh:
    if line.startswith("From "):
        line = line.rstrip()
        words = line.split()
        lst.append(words[1])
for emails in lst:
    counts[emails] = counts.get(emails,0) + 1
#print(counts)
# {'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 3, 'zqian@umich.edu': 4, 'rjlowe@iupui.edu': 2, 'cwen@iupui.edu': 5, 'gsilver@umich.edu': 3, 'wagnermr@iupui.edu': 1, 'antranig@caret.cam.ac.uk': 1, 'gopal.ramasammycook@gmail.com': 1, 'david.horwitz@uct.ac.za': 4, 'ray@media.berkeley.edu': 1}

count = None
most_repeated_email = None
for key,value in counts.items():
    if count is None or value > count:
        count = value
        most_repeated_email = key
print(most_repeated_email, count)

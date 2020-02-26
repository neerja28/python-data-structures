# Prog without using the sum function
fh = open("short-mb.txt")
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    fnum = line[20:26].rstrip()
    value = float(fnum)
    total = total + value
    count = count + 1
average = total/count
print(average)
print('Average spam confidence: ', average)

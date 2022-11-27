# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
tot = 0
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    find = line.find(':')
    num = line[find+1:]
    fnum = float(num)
    tot = tot + (fnum)
    avrg = tot/count
print('Average spam confidence:',avrg)
  


fname = input('Enter file name: ')
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
counts = dict()

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    counts[words[1]] = counts.get(words[1],0) + 1
max_sender = None
max_num = None
for key,value in counts.items():
    if max_num is None or max_num < value:
        max_sender = key
        max_num = value
print(max_sender,max_num)

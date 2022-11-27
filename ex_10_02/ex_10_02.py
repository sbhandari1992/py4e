fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)

hr_count = dict()
hr_list = list()

for line in fh:
    words = line.split()
    #print(words)
    #print(len(words))
    if len(words) > 2 and words[0] == 'From':
        peice = words[5]
        hr = peice.split(':')
        hr_count[hr[0]] = hr_count.get(hr[0],0) + 1
#print(hr_count)
for k,v in hr_count.items():
    hr_list.append((k,v))
#print(hr_list)
hr_list.sort()
#print(hr_list)
for k,v in hr_list:
    print(k,v)

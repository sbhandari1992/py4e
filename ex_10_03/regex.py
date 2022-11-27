mport re
tot = 0
fh = open('regex_sum_1366404.txt')
for line in fh:
    lst = re.findall('[0-9]+',line)
    for i in lst:
        num = int(i)
        tot = tot + num
print(tot)

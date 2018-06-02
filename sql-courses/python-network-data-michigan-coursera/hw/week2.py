import re

numlist = []
#hand = open('regex_sum_42.txt','r')
hand = open('regex_sum_292929.txt','r')
for line in hand:
#    line = line.rstrip()
    if re.search('[0-9]+',line):
        stuff = re.findall('[0-9]+',line)
        for strs in stuff:
            numlist.append(float(strs))
#        num = float(stuff[0])
#        numlist.append(num)
print len(numlist)
print sum(numlist)

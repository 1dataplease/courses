import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

headr = urllib.request.Request.get_header('http://www.py4inf.com/code/romeo.txt')

for line in fhand:
    print line.strip()
    
print headr
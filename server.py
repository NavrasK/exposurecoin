from urllib.request import urlopen
from urllib.request import urlretrieve

text = urlopen("http://www.brokenmirror.ca/test.txt")
for line in text:
    print(str(line.rstrip().decode()))


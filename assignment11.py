import csv
import re

filename = r'C:\Users\ASUS\Desktop\Py4e1\regex_sum_1206550.txt'
f = open(filename)
d = f.read()
y = re.findall('[0-9]+', d)
sum = 0
for i in range(len(y)):
    c = int(y[i])
    sum += c

print(sum)

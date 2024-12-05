import re

sum_of_mul = 0

with open('input2.txt') as f:
    line = f.read()

lst = re.findall(r"mul\([0-9]+,[0-9]+\)", line)

for mul in lst:
    temp = re.sub("[^0-9+,]", "", mul)
    s = re.split(",", temp)
    sum_of_mul += int(s[0]) * int(s[1])

print(sum_of_mul)




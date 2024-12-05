count = 0


def count_xmas(strng):
    return strng.count('XMAS') + strng.count('SAMX')


with open('input2.txt') as f:
    lines = f.read().splitlines()

#horizontal
for line in lines:
    count += count_xmas(line)

#vertical
for x in range(len(lines[0])):
    s = ''
    for y in range(len(lines)):
        s += lines[y][x]
    count += count_xmas(s)

#diagonal left-to-right
for i in range(len(lines[0])):
    y = 0
    s = ''
    for x in range(i, -1, -1):
        s += lines[y][x]
        y += 1
    count += count_xmas(s)
for i in range(1, len(lines)):
    x = len(lines[0]) - 1
    s = ''
    for y in range(i, len(lines)):
        s += lines[y][x]
        x -= 1
    count += count_xmas(s)

#diagonal right-to-left
for i in range(len(lines)):
    x = 0
    s = ''
    for y in range(i,len(lines)):
        s += lines[y][x]
        x += 1
    count += count_xmas(s)
for i in range(1, len(lines[0])):
    y = 0
    s = ''
    for x in range(i, len(lines[0])):
        s += lines[y][x]
        y += 1
    count += count_xmas(s)

print(count)
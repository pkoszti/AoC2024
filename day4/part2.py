count = 0

points = [[-1, 1], [1, 1], [1, -1], [-1, -1]]
m = 'M'
s = 'S'

with open('input2.txt') as f:
    lines = f.read().splitlines()

for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == 'A' and 0 < x < len(lines[0]) - 1 and 0 < y < len(lines) - 1:
            lst = []
            for point in points:
                lst.append(lines[y + point[0]][x + point[1]])
            if lst.count(s) == lst.count(m) == 2 and (s + s in "".join(lst) or m + m in "".join(lst)):
                count += 1

print(count)
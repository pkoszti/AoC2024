import re
from functools import reduce

quadrants = [0, 0, 0, 0]
seconds = 100
limit = (101, 103)

with open('input2.txt') as f:
    for line in f:
        robot = [list(map(int, re.split(',', re.sub(r'[pv=]', '', l)))) for l in line.strip().split()]
        pos = robot[0]
        v = robot[1]
        pos[0] = (pos[0] + seconds * v[0]) % limit[0]
        pos[1] = (pos[1] + seconds * v[1]) % limit[1]

        if pos[0] in range(int(limit[0] / 2)) and pos[1] in range(int(limit[1] / 2)):
            quadrants[0] += 1
        elif pos[0] in range(int(limit[0] / 2) + 1, limit[0]) and pos[1] in range(int(limit[1] / 2)):
            quadrants[1] += 1
        elif pos[0] in range(int(limit[0] / 2)) and pos[1] in range(int(limit[1] / 2) + 1, limit[1]):
            quadrants[2] += 1
        elif pos[0] in range(int(limit[0] / 2) + 1, limit[0]) and pos[1] in range(int(limit[1] / 2) + 1, limit[1]):
            quadrants[3] += 1

print(reduce(lambda a, b: a * b, quadrants))
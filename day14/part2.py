import re
from collections import Counter
limit = (101, 103)
sec = 1
while True:
    plot = [[0 for i in range(limit[0])] for j in range(limit[1])]
    with open('input2.txt') as f:
        for line in f:
            robot = [list(map(int, re.split(',', re.sub(r'[pv=]', '', l)))) for l in line.strip().split()]
            pos = robot[0]
            v = robot[1]
            pos[0] = (pos[0] + sec * v[0]) % limit[0]
            pos[1] = (pos[1] + sec * v[1]) % limit[1]
            plot[pos[1]][pos[0]] += 1

    tmp = []
    for line in plot:
        tmp.extend(line)
    counter = Counter(tmp)
    if all(key < 2 for key in counter.keys()):
        print(sec)
        for line in plot:
            s = ''
            for c in line:
                if c == 0:
                    s += ' '
                else:
                    s += 'X'
            print(s)
    sec += 1

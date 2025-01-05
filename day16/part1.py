plot, cache = [], {}
dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
w = 10000000

with open('input3.txt') as f:
    for y, line in enumerate(f):
        if 'S' in line:
            start = (y, line.index('S'))
        if 'E' in line:
            end = (y, line.index('E'))
        plot.append([c for c in line.strip()])
        for x in range(len(line)):
            if line[x] in 'SE.':
                cache.update({(y, x): {0: w, 1: w, 2: w, 3: w}})

#[score, dir, [visited]]
paths = [[0, 1, [start]]]
while paths:
    path = paths.pop()
    curr_pos = path[2][-1]
    if path[0] < cache[curr_pos][path[1]]:
        cache[curr_pos][path[1]] = path[0]
        if curr_pos != end:
            for i in range(4):
                next_y = curr_pos[0] + dirs[i][0]
                next_x = curr_pos[1] + dirs[i][1]
                if plot[next_y][next_x] in 'SE.' and (next_y, next_x) not in path[2]:
                    paths.append([path[0] + 1 if i == path[1] else path[0] + 1001, i, path[2] + [(next_y, next_x)]])

print(min(cache[end].values()))



plot, pos, moves = [], [], ''
dir_vert, dir_horiz = '^v', '<>'
dir_all = (-1, 1)

with open('input3.txt') as f:
    for j, line in enumerate(f):
        if '#' in line:
            s = ''
            for c in line:
                match c:
                    case '#' | '.':
                        s += c * 2
                    case 'O':
                        s += '[]'
                    case '@':
                        pos = [j, len(s)]
                        s += '@.'
            plot.append([c for c in s])
        if '<' in line:
            moves += line.strip()


def go_vert(rng, direction):
    c = plot[pos[0] + direction][pos[1]]
    if c == '.':
        plot[pos[0] + direction][pos[1]] = '@'
        plot[pos[0]][pos[1]] = '.'
        pos[0] += direction
    elif c in '[]':
        pts = [(pos[0] + direction, pos[1], plot[pos[0] + direction][pos[1]])]
        queue = pts.copy()
        while queue:
            curr = queue.pop()
            if curr[2] == ']' and (curr[0], curr[1] - 1, '[') not in pts:
                pts.append((curr[0], curr[1] - 1, '['))
                queue.append((curr[0], curr[1] - 1, '['))
            if curr[2] == '[' and (curr[0], curr[1] + 1, ']') not in pts:
                pts.append((curr[0], curr[1] + 1, ']'))
                queue.append((curr[0], curr[1] + 1, ']'))
            if plot[curr[0] + direction][curr[1]] == '#':
                return
            elif plot[curr[0] + direction][curr[1]] in '[]':
                pts.append((curr[0] + direction, curr[1], plot[curr[0] + direction][curr[1]]))
                queue.append((curr[0] + direction, curr[1], plot[curr[0] + direction][curr[1]]))
        for p in pts:
            plot[p[0]][p[1]] = '.'
        for p in pts:
            plot[p[0] + direction][p[1]] = p[2]
        plot[pos[0] + direction][pos[1]] = '@'
        plot[pos[0]][pos[1]] = '.'
        pos[0] += direction


def go_horiz(rng, direction):
    lst = [plot[pos[0]][x] for x in rng]
    if '.' in lst:
        if lst.index('.') < lst.index('#'):
            lst.remove('.')
            lst.insert(0, '.')
            for x, p in zip(rng, lst):
                plot[pos[0]][x] = p
            pos[1] += direction


w = 0
for move in moves:
    if move in dir_horiz:
        rng_horiz = [range(pos[1], -1, -1), range(pos[1], len(plot[0]))]
        index = dir_horiz.index(move)
        go_horiz(rng_horiz[index], dir_all[index])
    else:
        rng_vert = [range(pos[0], -1, -1), range(pos[0], len(plot))]
        index = dir_vert.index(move)
        go_vert(rng_vert[index], dir_all[index])


sum_coord = 0
for y in range(len(plot)):
    for x in range(len(plot[0])):
        if plot[y][x] == '[':
            sum_coord += 100 * y + x
print(sum_coord)

plot, pos, moves = [], [], ''
dir_vert, dir_horiz = '^v', '<>'
dir_all = [-1, 1]

with open('input3.txt') as f:
    for j, line in enumerate(f):
        if '#' in line:
            if '@' in line:
                pos = [j, line.index('@')]
            plot.append([char for char in line.strip()])
        if '<' in line:
            moves += line.strip()


def go_vert(rng, direction):
    tmp = go([plot[y][pos[1]] for y in rng])
    if tmp:
        for y, p in zip(rng, tmp):
            plot[y][pos[1]] = p
        pos[0] += direction


def go_horiz(rng, direction):
    tmp = go([plot[pos[0]][x] for x in rng])
    if tmp:
        for x, p in zip(rng, tmp):
            plot[pos[0]][x] = p
        pos[1] += direction


def go(lst):
    if '.' in lst:
        if lst.index('.') < lst.index('#'):
            lst.remove('.')
            lst.insert(0, '.')
            return lst
    return []


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
        if plot[y][x] == 'O':
            sum_coord += 100 * y + x
print(sum_coord)

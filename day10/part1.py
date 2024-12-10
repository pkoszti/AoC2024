hiking_map, trailheads = [], []
go_y = [-1, 0, 1, 0]
go_x = [0, 1, 0, -1]
sum_of_scores = 0

y = 0
with open('input2.txt') as f:
    for line in f.read().splitlines():
        hiking_map.append(list(map(int, line)))
        for x in range(len(hiking_map[y])):
            if hiking_map[y][x] == 0:
                trailheads.append([y, x])
        y += 1


def save_point(point):
    return point[0] * 100 + point[1]


def go(pos):
    temp = []
    curr_val = hiking_map[pos[0]][pos[1]]
    for i in range(4):
        next_y = pos[0] + go_y[i]
        next_x = pos[1] + go_x[i]
        next_p = [next_y, next_x]
        if next_y in range(len(hiking_map)) and next_x in range(len(hiking_map[0])):
            next_val = hiking_map[next_y][next_x]
            if save_point(next_p) not in visited and next_val - curr_val == 1:
                temp.append(next_p)
                visited.append(save_point(next_p))
    return temp


for head in trailheads:
    score = 0
    visited = [save_point(head)]
    positions = [head]
    while positions:
        curr_pos = positions.pop()
        if hiking_map[curr_pos[0]][curr_pos[1]] == 9:
            score += 1
        else:
            positions.extend(go(curr_pos))
    sum_of_scores += score

print(sum_of_scores)

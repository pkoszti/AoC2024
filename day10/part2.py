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


def go(trail):
    temp = []
    curr_pos = trail[0]
    visited = trail[1]
    curr_val = hiking_map[curr_pos[0]][curr_pos[1]]
    for i in range(4):
        next_y = curr_pos[0] + go_y[i]
        next_x = curr_pos[1] + go_x[i]
        next_p = [next_y, next_x]
        if next_y in range(len(hiking_map)) and next_x in range(len(hiking_map[0])):
            next_val = hiking_map[next_y][next_x]
            if save_point(next_p) not in visited and next_val - curr_val == 1:
                next_trail = [next_p, [*visited]]
                next_trail[1].append(save_point(next_p))
                temp.append(next_trail)
    return temp


for head in trailheads:
    paths = set()
    trails = [[head, [save_point(head)]]]
    while trails:
        curr_trail = trails.pop()
        if hiking_map[curr_trail[0][0]][curr_trail[0][1]] != 9:
            next_points = go(curr_trail)
            trails.extend(next_points)
        else:
            sum_of_scores += 1

print(sum_of_scores)

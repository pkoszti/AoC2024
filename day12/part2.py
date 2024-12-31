go_y = [-1, 0, 1, 0]
go_x = [0, 1, 0, -1]
go_xy = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0))
price = 0

with open('input2.txt') as f:
    plot = f.read().splitlines()

visited = [[False for i in range(len(plot[0]))] for j in range(len(plot))]

for y in range(len(plot)):
    for x in range(len(plot[0])):
        if not visited[y][x]:
            plant = plot[y][x]
            region = {}
            queue = [(y, x)]
            while queue:
                curr_p = queue.pop()
                visited[curr_p[0]][curr_p[1]] = True
                tmp = []
                for i in range(4):
                    next_y = curr_p[0] + go_y[i]
                    next_x = curr_p[1] + go_x[i]
                    if 0 <= next_y < len(plot) and 0 <= next_x < len(plot[0]) and plot[next_y][next_x] == plant:
                        tmp.append((next_y, next_x))
                for p in tmp:
                    if not visited[p[0]][p[1]]:
                        queue.append(p)
                region.update({curr_p: tmp})

            edges = 0
            for p in region.keys():
                conns = region[p]
                l = len(conns)
                if l == 0:
                    edges = 4
                    break
                elif l == 1:
                    edges += 2
                else:
                    if l == 2 and conns[0][0] != conns[1][0] and conns[0][1] != conns[1][1]:
                        edges += 1
                    for i in range(0, 8, 2):
                        p1 = (p[0] + go_xy[i][0], p[1] + go_xy[i][1])
                        p2 = (p[0] + go_xy[i + 1][0], p[1] + go_xy[i + 1][1])
                        p3 = (p[0] + go_xy[i + 2][0], p[1] + go_xy[i + 2][1])
                        if {p1, p3}.issubset(region.keys()) and p2 not in region.keys():
                            edges += 1
            price += edges * len(region.keys())

print(price)

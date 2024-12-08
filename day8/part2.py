plot, antennas = [], {}


i = 0
with open('input2.txt') as f:
    for line in f.read().splitlines():
        plot.append(line)
        for x in range(len(line)):
            if line[x] != '.':
                if line[x] in antennas.keys():
                    antennas.get(line[x]).append((i, x))
                else:
                    antennas.update({line[x]: [(i, x)]})
        i += 1

antinodes = set()
for points in antennas.values():
    for i in range(len(points)):
        for j in range(len(points)):
            if i != j:
                point1, point2 = points[i], points[j]
                y_diff, x_diff = point2[0] - point1[0], point2[1] - point1[1]
                curr_y, curr_x = point2[0] + y_diff, point2[1] + x_diff
                while 0 <= curr_y < len(plot) and 0 <= curr_x < len(plot[0]):
                    antinodes.add((curr_y, curr_x))
                    curr_y += y_diff
                    curr_x += x_diff
                antinodes.update(points)

print(len(antinodes))

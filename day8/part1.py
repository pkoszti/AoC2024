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
                next_y = 2 * point2[0] - point1[0]
                next_x = 2 * point2[1] - point1[1]
                if 0 <= next_y < len(plot) and 0 <= next_x < len(plot[0]):
                    antinodes.add((next_y, next_x))

print(len(antinodes))

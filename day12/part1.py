go_y = [-1, 0, 1, 0]
go_x = [0, 1, 0, -1]

with open('input2.txt') as f:
    plot = f.read().splitlines()

regions = {}
sum_of_prices = 0

for y in range(len(plot)):
    for x in range(len(plot[0])):
        curr_plant = plot[y][x]
        curr_point = (y, x)
        if curr_plant not in regions.keys():
            regions[curr_plant] = []
        if curr_point not in regions[curr_plant]:
            fence = 0
            curr_region = [curr_point]
            curr_points = [curr_point]
            while curr_points:
                curr_point = curr_points.pop()
                for i in range(4):
                    next_y = curr_point[0] + go_y[i]
                    next_x = curr_point[1] + go_x[i]
                    if 0 <= next_y < len(plot) and 0 <= next_x < len(plot[0]) and plot[next_y][next_x] == curr_plant:
                        if (next_y, next_x) not in curr_region:
                            curr_region.append((next_y, next_x))
                            curr_points.append((next_y, next_x))
                    else:
                        fence += 1
            sum_of_prices += fence * len(curr_region)
            regions[curr_plant].extend(curr_region)

print(sum_of_prices)

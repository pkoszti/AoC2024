go_x = [0, 1, 0, -1]
go_y = [-1, 0, 1, 0]
sum_of_loops = 0

with open('input2.txt') as f:
    guard = f.read().splitlines()

visited = set()
start_y = start_x = 0
for i in range(len(guard)):
    if '^' in guard[i]:
        start_y = i
        start_x = guard[i].index('^')
        visited.add((start_y, start_x))

way = 0
curr_y, curr_x = start_y, start_x
next_y, next_x = curr_y + go_y[way], curr_x + go_x[way]
while 0 <= next_y < len(guard) and 0 <= next_x < len(guard[0]):
    if guard[next_y][next_x] == '#':
        way = way + 1 if way < 3 else 0
    else:
        curr_y, curr_x = next_y, next_x
        visited.add((curr_y, curr_x))
    next_y, next_x = curr_y + go_y[way], curr_x + go_x[way]

for point in visited:
    if point != (start_y, start_x):
        way = 0
        curr_y, curr_x = start_y, start_x
        next_y, next_x = curr_y + go_y[way], curr_x + go_x[way]
        visited_loop = [(curr_y, curr_x, 0)]
        while 0 <= next_y < len(guard) and 0 <= next_x < len(guard[0]):
            if (next_y, next_x, way) in visited_loop:
                sum_of_loops += 1
                break
            elif guard[next_y][next_x] == '#' or (next_y, next_x) == point:
                way = way + 1 if way < 3 else 0
            else:
                curr_y, curr_x = next_y, next_x
                visited_loop.append((curr_y, curr_x, way))
            next_y, next_x = curr_y + go_y[way], curr_x + go_x[way]

print(sum_of_loops)

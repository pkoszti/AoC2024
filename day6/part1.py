go_x = [0, 1, 0, -1]
go_y = [-1, 0, 1, 0]

with open('input2.txt') as f:
    guard = f.read().splitlines()

visited = set()
curr_y = curr_x = 0
for i in range(len(guard)):
    if '^' in guard[i]:
        curr_y = i
        curr_x = guard[i].index('^')
        visited.add((curr_y, curr_x))

way = 0
next_y, next_x = curr_y + go_y[way], curr_x + go_x[way]
while 0 <= next_y < len(guard) and 0 <= next_x < len(guard[0]):
    if guard[next_y][next_x] == '#':
        way = way + 1 if way < 3 else 0
    else:
        curr_y, curr_x = next_y, next_x
        visited.add((curr_y, curr_x))
    next_y, next_x = curr_y + go_y[way], curr_x + go_x[way]

print(len(visited))

with open('input2.txt') as f:
    disk_map = f.read().strip()

#0-occurances of ID, 1-ID
lst1, lst2 = [], []
j = sum_of_empty = 0
for i in range(0, len(disk_map), 2):
    lst1.append((int(disk_map[i]), j))
    if i + 1 < len(disk_map) and int(disk_map[i + 1]) > 0:
        empty = int(disk_map[i + 1])
        lst1.append(empty)
        sum_of_empty += empty
    j += 1

i = 0
while sum_of_empty > 0:
    if type(lst1[i]) == int:
        curr_empty = lst1[i]
        curr_tail = lst1.pop()
        while curr_empty > 0:
            if type(curr_tail) == int:
                sum_of_empty -= curr_tail
                curr_tail = lst1.pop()
            else:
                if curr_empty > curr_tail[0]:
                    sum_of_empty -= curr_tail[0]
                    lst2.append(curr_tail)
                    curr_empty -= curr_tail[0]
                    curr_tail = lst1.pop()
                elif curr_empty == curr_tail[0]:
                    sum_of_empty -= curr_tail[0]
                    lst2.append(curr_tail)
                    curr_empty = 0
                else:
                    sum_of_empty -= curr_empty
                    lst2.append((curr_empty, curr_tail[1]))
                    lst1.append((curr_tail[0] - curr_empty, curr_tail[1]))
                    curr_empty = 0
    else:
        lst2.append(lst1[i])
    i += 1
lst2.extend(lst1[i:len(lst1)])

checksum = i = 0
for item in lst2:
    for j in range(item[0]):
        checksum += i * item[1]
        i += 1

print(checksum)
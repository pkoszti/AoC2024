with open('input2.txt') as f:
    disk_map = f.read().strip()

# 0-occurances of ID, 1-ID
lst = []
j = files_count = 0
for i in range(0, len(disk_map), 2):
    lst.append((int(disk_map[i]), j))
    files_count += 1
    if i + 1 < len(disk_map) and int(disk_map[i + 1]) > 0:
        empty = int(disk_map[i + 1])
        lst.append((empty,))
    j += 1


def is_file(tpl):
    return len(tpl) == 2


i = len(lst) - 1
while files_count > 0:
    if is_file(lst[i]):
        curr_item = lst[i]
        for j in range(i):
            if not is_file(lst[j]) and lst[j][0] >= curr_item[0]:
                curr_empty = lst[j][0]
                if curr_empty == curr_item[0]:
                    lst[i] = (curr_empty,)
                    lst[j] = curr_item
                    i -= 1
                else:
                    lst[i] = (curr_item[0],)
                    lst[j] = (curr_empty - curr_item[0],)
                    lst.insert(j, curr_item)
                break
        else:
            i -= 1
        files_count -= 1
    else:
        i -= 1

checksum = i = 0
for item in lst:
    for j in range(item[0]):
        checksum += i * item[1] if len(item) == 2 else 0
        i += 1

print(checksum)

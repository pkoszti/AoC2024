with open('input2.txt') as f:
    stones = dict.fromkeys(map(int, f.read().strip().split()), 1)


def add_stone(stn):
    if stn in temp.keys():
        temp[stn] += amount
    else:
        temp[stn] = amount


blinks = 25
for i in range(0, blinks):
    x = len(stones)
    temp = {}
    for stone, amount in stones.items():
        if amount > 0:
            if stone == 0:
                add_stone(1)
            elif len(str(stone)) % 2 == 0:
                s = str(stone)
                add_stone(int(s[:int(len(s) / 2)]))
                add_stone(int(s[int(len(s) / 2):]))
            else:
                add_stone(stone * 2024)
    stones = temp

print(sum(stones.values()))

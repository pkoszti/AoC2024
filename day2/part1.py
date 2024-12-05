sum_of_safe = 0

with open('input2.txt') as f:
    for line in f:
        levels = [int(x) for x in line.split()]
        sorted_levels = sorted(levels)
        sorted_levels_rev = sorted(levels, reverse=True)

        if levels == sorted_levels or levels == sorted_levels_rev:
            for x in range(len(levels) - 1):
                if not abs(levels[x] - levels[x + 1]) in range(1, 4):
                    break
            else:
                sum_of_safe += 1

print(sum_of_safe)

sum_of_safe = 0


def is_safe(levels):
    sorted_levels = sorted(levels)
    sorted_levels_rev = sorted_levels[::-1]

    if levels == sorted_levels or levels == sorted_levels_rev:
        for x in range(len(levels) - 1):
            if not abs(levels[x] - levels[x + 1]) in range(1, 4):
                return False
        else:
            return True


with open('input3.txt') as f:
    for line in f:
        levels = [int(x) for x in line.split()]
        if is_safe(levels):
            sum_of_safe += 1
        else:
            for x in range(len(levels)):
                levels2 = levels.copy()
                del levels2[x]
                if is_safe(levels2):
                    sum_of_safe += 1
                    break

print(sum_of_safe)

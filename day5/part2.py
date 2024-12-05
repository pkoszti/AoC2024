import re
from functools import cmp_to_key

rules, updates = [], []
sum_middle = 0

with open('input2.txt') as f:
    for line in f.read().splitlines():
        if '|' in line:
            rules.append([int(i) for i in re.split(r'\|', line)])
        if ',' in line:
            updates.append([int(i) for i in re.split(r',', line)])


def compare(page1, page2):
    for rule in rules:
        if page1 in rule and page2 in rule:
            return rule.index(page1) - rule.index(page2)


for update in updates:
    update_sorted = sorted(update.copy(), key=cmp_to_key(compare))
    if not update == update_sorted:
        sum_middle += update_sorted[int(len(update_sorted) / 2)]

print(sum_middle)
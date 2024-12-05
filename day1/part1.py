list1 = []
list2 = []
sum_of_dist = 0

with open('input2.txt') as f:
    for line in f:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))

list1 = sorted(list1)
list2 = sorted(list2)

for x in range(len(list1)):
    sum_of_dist += abs(list2[x] - list1[x])

print(sum_of_dist)
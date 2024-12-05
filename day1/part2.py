import collections

list1 = []
list2 = []
sum_of_similarity = 0

with open('input2.txt') as f:
    for line in f:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))

counter2 = collections.Counter(list2)

for id_no in list1:
    sum_of_similarity += id_no * counter2[id_no]

print(sum_of_similarity)
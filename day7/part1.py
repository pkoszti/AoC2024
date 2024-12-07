sum_of_test = 0

with open('input2.txt') as f:
    for line in f.read().replace(":", "").splitlines():
        test_val = int(line.split()[0])
        nums = [int(num) for num in line.split()[1:]]
        vals = [nums[0]]
        for i in range(1, len(nums)):
            temp = []
            while len(vals) != 0:
                curr_val = vals.pop()
                temp.append(curr_val + nums[i])
                temp.append(curr_val * nums[i])
            vals.extend(temp)
        if test_val in vals:
            sum_of_test += test_val

print(sum_of_test)
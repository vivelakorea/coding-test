def p2108(nums):
    nums.sort()
    average = sum(nums) // len(nums)
    if ( sum(nums) / len(nums) )% 1 >= 0.5:
        average += 1
    median = nums[len(nums) // 2]

    count = {}
    for num in nums:
        if num not in count:
            count[num] = 0
        count[num] += 1
    count_arr = []
    for num in count:
        count_arr.append((count[num], num))
    count_arr.sort(reverse=True)
    max_count = count_arr[0][0]
    i = 0
    while i < len(count_arr) and count_arr[i][0] == max_count:
        i += 1
    max_count_nums = []
    for j in range(i):
        max_count_nums.append(count_arr[j][1])
    max_count_nums.sort()
    if len(max_count_nums) > 1:
        mode = max_count_nums[1]
    else:
        mode = max_count_nums[0]

    r = nums[-1] - nums[0]

    return average, median, mode, r


nums = []
for _ in range(int(input())):
    nums.append(int(input()))

for ans in p2108(nums):
    print(ans)
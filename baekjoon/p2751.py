def p2751(nums):
    # counting sort
    # 1 <= num <= 10000000
    counts = [0] * 10000001 # counts[i] == i 갯수
    accumul_counts = [0] * 10000001
    for num in nums:
        counts[num] += 1
    for i in range(1, 10000001):
        accumul_counts[i] = accumul_counts[i - 1] + counts[i]
    B = [0] * (len(nums) + 1)
    for i in range(len(nums)-1, -1, -1):
        B[accumul_counts[nums[i]]] = nums[i]
        accumul_counts[nums[i]] -= 1
    return B
            

T = int(input())
nums = []
for _ in range(T):
    nums.append(int(input()))
for num in p2751(nums):
    print(num)

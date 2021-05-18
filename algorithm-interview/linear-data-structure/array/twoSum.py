import collections
class Solution:
    def twoSum(self, nums, target):
        hashmap = collections.defaultdict(list)
        for i, num in enumerate(nums):
            hashmap[num].append(i)
        for num in hashmap:
            if target - num in hashmap:
                if target - num == num and len(hashmap[target - num]) != 1:
                    return [hashmap[num][0], hashmap[target - num][1]]
                elif target - num != num:
                    return [hashmap[num][0], hashmap[target - num][0]]

s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))


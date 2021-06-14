import random
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, j, k = 0, 0, len(nums)
        mid = 1
        while j < k:
            if nums[j] > mid:
                k -= 1
                nums[j], nums[k] = nums[k], nums[j]
            elif nums[j] < mid:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                j += 1

s = Solution()
for i in range(1, 100):
    nums = [0] * random.randrange(0, i) + [1] * random.randrange(0, i) + [2] * random.randrange(0, i)
    random.shuffle(nums)
    s.sortColors(nums)
    print(sorted(nums) == nums)
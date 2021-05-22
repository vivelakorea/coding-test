from typing import List

class Solution:
    def even(self):
        n = 0
        while True:
            yield n
            n += 2
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        g = self.even()
        s = 0
        while True:
            try:
                s += nums[next(g)]
            except:
                break
        return s

s = Solution()
print(s.arrayPairSum([6,2,6,5,1,2]))
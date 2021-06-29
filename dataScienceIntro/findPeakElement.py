from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def find(left, right):
            # left 이상, right 미만 내에서 찾기
            if left >= right:
                return -1
            mid = (left + right) // 2
            if mid + 1 < len(nums) and nums[mid] < nums[mid + 1]:
                return find(mid + 1, right)
            elif mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                return find(left, mid)
            else:
                return mid
        return find(0, len(nums))

s = Solution()
print(s.findPeakElement([1,2,3,1]))
print(s.findPeakElement([1,2,1,3,5,6,4]))
print(s.findPeakElement([1]))
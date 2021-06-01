from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from_left, from_right = [1], [1]
        for num in nums[:len(nums)-1]:
            from_left.append(from_left[-1] * num)
        for num in nums[:0:-1]:
            from_right.append(from_right[-1] * num)
        products = []
        for i in range(len(nums)):
            products.append(from_left[i] * from_right[len(nums) - i - 1])
        return products

s = Solution()
print(s.productExceptSelf([-1,1,0,-3,3]))
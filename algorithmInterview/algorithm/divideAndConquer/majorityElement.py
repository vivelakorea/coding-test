# https://leetcode.com/problems/majority-element/submissions/

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def majorityElement__helper(nums: List[int]) -> (int, int):
            n = len(nums)
            if n == 1:
                return nums[0]
            leftNum = majorityElement__helper(nums[:n//2]) 
            rightNum = majorityElement__helper(nums[n//2:])
            if (nums.count(leftNum) > nums.count(rightNum)):
                return leftNum
            return rightNum
        
        return majorityElement__helper(nums)
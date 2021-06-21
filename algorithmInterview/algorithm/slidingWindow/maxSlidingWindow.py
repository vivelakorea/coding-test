from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = nums[:k]
        max_index = window.index(max(window))
        res.append(window[max_index])
        for i in range(len(nums) - k):
            # current window : nums[i:i+k]
            # next window : nums[i+1:i+k+1]
            # print(nums[i:i+k])
            # print(nums[i+1:i+k+1])
            if max_index == i:
                # print("research")
                window = nums[i+1:i+k+1]
                max_index = i + 1 + window.index(max(window))
            else:
                # print("compare")
                if nums[max_index] < nums[i+k]:
                    max_index = i + k
            # print("i = {}, max_index = {}".format(i, max_index))
            res.append(nums[max_index])
        return res

s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) # 1 4 4 6 7
print(s.maxSlidingWindow([1], 1))
print(s.maxSlidingWindow([1,-1], 1))
print(s.maxSlidingWindow([9,11], 2))
print(s.maxSlidingWindow([4,-2], 2))
print(s.maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4))
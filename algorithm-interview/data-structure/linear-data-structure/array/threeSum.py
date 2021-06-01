from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        triplets = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else: # nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
        return triplets
        # result = []
        # hashset = set()
        # for triplet in triplets:
        #     hashvalue = hash(str(triplet))
        #     print(triplet, hashvalue)
        #     if hashvalue not in hashset:
        #         result.append(triplet)
        #         hashset.add(hashvalue)
        # return result
                

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
        
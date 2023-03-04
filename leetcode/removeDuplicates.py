class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count k
        memory = nums[0]
        k = 1
        for i in range(1, len(nums)):
            if memory != nums[i]:
                memory = nums[i]
                k += 1
        # swap
        place = 1
        memory = nums[0]
        i = 1
        while place < k:
            if memory != nums[i]:
                memory = nums[i]
                nums[place] = nums[i]
                place += 1
            i += 1
        return k

data = [1,10,10,20,20,20]
print(Solution().removeDuplicates(data), data)
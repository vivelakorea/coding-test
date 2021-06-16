class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 # 0은 xor에 대한 항등원
        for num in nums:
            res ^= num
        return res


s = Solution()
print(s.singleNumber([2,2,1]))
print(s.singleNumber([4,1,2,1,2]))
print(s.singleNumber([1]))
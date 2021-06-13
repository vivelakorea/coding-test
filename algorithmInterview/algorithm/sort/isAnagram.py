class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sum(hash(c) for c in s) == sum(hash(c) for c in t)

s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))
print(s.isAnagram("a", "ab"))
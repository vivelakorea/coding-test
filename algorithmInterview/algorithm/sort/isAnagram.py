class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashed1, hashed2 = 0, 0
        for c in s:
            hashed1 += hash(c)
        for c in t:
            hashed2 += hash(c)
        return hashed1 == hashed2

s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))
print(s.isAnagram("a", "ab"))
import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0


        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1
            

            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                
                if not end or end - start >= right - left:
                    start, end = left, right

                need[s[left]] += 1
                left += 1
                missing += 1
        return s[start: end]


        
            
s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
print(s.minWindow("abc", "bc"))
print(s.minWindow("a", "a"))
print(s.minWindow("a", "aa"))
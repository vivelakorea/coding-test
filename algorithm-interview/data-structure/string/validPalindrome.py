class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        for c in s:
            if c.isalnum():
                string.append(c.lower())
        return string == string[::-1]

s = Solution()
print(s.isPalindrome("0P"))
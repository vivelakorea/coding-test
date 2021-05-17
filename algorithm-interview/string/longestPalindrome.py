class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left: right] == s[left: right][::-1]:
                left -= 1
                right += 1
            return (left + 1, right - 1)

        if len(s) < 2 or s == s[::-1]:
            return s
        
        longest_pair = (0, 1)
        for i in range(len(s) - 1):
            l1, r1 = expand(i, i + 1) # 홀수 길이
            l2, r2 = expand(i, i + 2) # 짝수 길이
            if r1 - l1 > longest_pair[1] - longest_pair[0]:
                longest_pair = (l1, r1)
            if r2 - l2 > longest_pair[1] - longest_pair[0]:
                longest_pair = (l2, r2)
        
        return s[longest_pair[0]: longest_pair[1]]
                         
s = Solution()
print(s.longestPalindrome("abb"))
            
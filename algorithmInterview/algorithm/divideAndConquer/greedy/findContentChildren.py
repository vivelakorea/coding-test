# https://leetcode.com/problems/assign-cookies/submissions/

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        sorted_g = sorted(g)
        sorted_s = sorted(s)
        res = 0
        j = 0
        for i in range(len(sorted_g)):
            while j < len(sorted_s) and sorted_s[j] < sorted_g[i]:
                j += 1
            if j == len(sorted_s):
                break
            res += 1
            j += 1
        return res
import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, len(s)
        res = 0
        count = collections.Counter(s)
        num_max_character = count.most_common()[0][1]
        flag = True
        while left <= right:
            num_max_character = count.most_common()[0][1]
            print(left, right, num_max_character)
            if right - left - num_max_character <= k:
                res = max(res, right - left)
            if flag:
                count[s[left]] -= 1
                left += 1
                flag = False
            else:
                count[s[right - 1]] -= 1
                right -= 1
                flag = True
        return res


s = Solution()
# print(s.characterReplacement("ABAB", 2))
# print(s.characterReplacement("AABABBA", 1))
print(s.characterReplacement("AAAB", 0))

import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        # num_max_character = count.most_common()[0][1]
        def expand(left, right):
            count = collections.Counter(s[left:right+1])
            most_common = count.most_common()[0][1]
            while right < len(s) and right - left + 1 - most_common <= k:
                right += 1
                if right < len(s):
                    count[s[right]] += 1
                most_common = count.most_common()[0][1]
                # print('left', left, 'right', right, 'most_common', most_common, 'count.most_common()', count.most_common())

            # print('sdf',right - left)
            return right - left
        
        for left in range(len(s)):
            right = left + res
            if right > len(s):
                break
            res = max(res, expand(left, right))

        return res


s = Solution()
print(s.characterReplacement("ABAB", 2))
print(s.characterReplacement("AABABBA", 1))
print(s.characterReplacement("AAAB", 0))
print(s.characterReplacement("AABA", 0))

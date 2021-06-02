class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {}
        for i in range(len(s)):
            last_index[s[i]] = i
        
        stack = []
        seen = set()

        for i in range(len(s)):
            if s[i] in seen:
                continue
            while stack and s[i] < stack[-1] and last_index[stack[-1]] > i:
                seen.remove(stack.pop())
            stack.append(s[i])
            seen.add(s[i])
        
        return ''.join(stack)

s = Solution()
print(s.removeDuplicateLetters("bcabc"))
print(s.removeDuplicateLetters("cbacdcbc"))
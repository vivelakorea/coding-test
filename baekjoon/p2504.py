class Solution:
    def parenthesisScore(self, line):
        char_stack = []
        score_stack = [0]

        balanced = True

        ref = {
            ')': ('(', 2),
            ']': ('[', 3)
        }

        for c in line:
            if c in ref:
                if not char_stack or char_stack.pop() != ref[c][0]:
                    return 0
                else:
                    if score_stack[-1] == 0:
                        score_stack.pop()
                        score_stack[-1] += ref[c][1]
                    else:
                        popped = score_stack.pop()
                        score_stack[-1] += popped * ref[c][1]
            else: # '(' or '['
                char_stack.append(c)
                score_stack.append(0)

        if char_stack:
            return 0
        return score_stack[0]

s = Solution()
print(s.parenthesisScore(input()))
# print(s.parenthesisScore('(()[[]])([])'))
# print(s.parenthesisScore('[][]((])'))
# print(s.parenthesisScore('('))
# print(s.parenthesisScore(')'))
# print(s.parenthesisScore('()[()]'))
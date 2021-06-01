class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for c in s:
            if c not in map: # '(', '{', '['
                stack.append(c)
            else:            # ')', '}', ']'
                if not stack or map[c] != stack.pop():
                    return False
        return len(stack) == 0

s = Solution()
print(not s.isValid("(")) 
print(not s.isValid(")")) 
print(s.isValid("()")) 
print(not s.isValid(")(")) 
print(not s.isValid("(}")) 
print(not s.isValid("([")) 
print(not s.isValid("(()")) 
print(s.isValid("(())")) 
print(s.isValid("[()]")) 
print(not s.isValid("()]"))
print(not s.isValid("[)(]"))
print(s.isValid("()[]{}"))
print(s.isValid("[()[]{}]"))
print(s.isValid("(()[{()}])"))
print(not s.isValid("(())[{()}])"))
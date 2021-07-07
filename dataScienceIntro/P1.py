import collections

def P1(s: str) -> bool:
    if len(s) % 2 == 1:
        return False

    ref = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    stack = collections.deque()
    for c in s:
        if c not in ref: # '(', '{', '['
            stack.append(c)
        else:            # ')', '}', ']'
            if not stack or ref[c] != stack.pop():
                return False
    return len(stack) == 0


print(P1('()'))
print(P1('()[]{}'))
print(P1('([)]'))
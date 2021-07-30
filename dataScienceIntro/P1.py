import collections

def P1(parentheses: str) -> bool:
    if len(parentheses) % 2 == 1:
        return False

    ref = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    stack = collections.deque()
    for c in parentheses:
        if c not in ref: # '(', '{', '['
            stack.append(c)
        else:            # ')', '}', ']'
            if not stack or ref[c] != stack.pop():
                return False
    return len(stack) == 0


# print(P1('()'))
# print(P1('()[]{}'))
# print(P1('([)]'))
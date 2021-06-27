line = input()

char_stack = []
score_stack = [0]

balanced = True

ref = {
    ')': ('(', 2),
    ']': ('[', 3)
}

for c in line:
    if c in ref:
        if char_stack.pop() != ref[c][0]:
            balanced = False
            break
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

if char_stack or not balanced:
    print('0')
else:
    print(score_stack[0])
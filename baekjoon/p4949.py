from sys import stdin

while True:
    line = stdin.readline()
    if line == '.\n':
        break

    stack = []
    ref = {
        ']': '[',
        ')': '('
    }
    balanced = True
    
    for c in line:
        if c in set(ref.values()):
            stack.append(c)
        elif c in ref and (not stack or stack.pop() != ref[c]):
            balanced = False
            break
    
    if stack or not balanced:
        print('no')
    else:
        print('yes')
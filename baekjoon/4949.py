from sys import stdin

while True:
    line = stdin.readline()
    if line == '.\n':
        break

    stack = []
    balanced = True
    ref = {
        ']': '[',
        ')': '('
    }
    
    for c in line:
        if c == '[' or c == '(':
            stack.append(c)
        elif c in ref and (not stack or stack.pop() != ref[c]):
            balanced = False
            break
    
    if stack or not balanced:
        print('no')
    else:
        print('yes')            
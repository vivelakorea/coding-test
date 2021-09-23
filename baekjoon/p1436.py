def p1436(N):
    count = 0
    i = 666
    while count < N:
        if '666' in str(i):
            count += 1
        i += 1
    return i - 1

print(p1436(int(input())))
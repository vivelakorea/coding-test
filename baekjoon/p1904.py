import collections
def p1904(N):
    f = collections.deque([1, 1])
    for i in range(2, N + 1):
        f.append(f[-1] + f[-2])
        f.popleft()
    return f[-1]
print(p1904(int(input())))
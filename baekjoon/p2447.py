import sys

def log3(n):
    i = 0
    while n != 1:
        n //= 3
        i += 1
    return i

def p2447(n):
    if log3(n) == 1:
        return [[1,1,1],
                [1,0,1],
                [1,1,1]]
    else:
        prev = p2447(n//3)
        res = []
        for _ in range(n):
            res.append([])
        # 1) for each row, x3
        for i in range(n//3):
            res[i].extend(prev[i][:])
            res[i].extend(prev[i][:])
            res[i].extend(prev[i][:])
        # 2) for each row, self + 0s + self
        for i in range(n//3, n//3 * 2):
            res[i].extend(prev[i - n//3][:])
            res[i].extend([0]*(n//3))
            res[i].extend(prev[i - n//3][:])
        # 3) for each row, x3
        for i in range(n//3 * 2, n):
            res[i].extend(prev[i - n//3 * 2][:])
            res[i].extend(prev[i - n//3 * 2][:])
            res[i].extend(prev[i - n//3 * 2][:])
        return res

N = int(sys.stdin.readline())

bin_format = p2447(N)

for row in bin_format:
    for b in row:
        if b == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print('\n', end='')
        
import sys

def partition_sum(n):
    tmp = n
    res = 0
    while n:
        res += n % 10
        n -= n % 10
        n //= 10
    res += tmp
    return res

def p2331(n):
    res = 1
    while res < n and partition_sum(res) != n:
        res += 1
    if res == n:
        return 0
    return res


N = int(sys.stdin.readline())
print(p2331(N))


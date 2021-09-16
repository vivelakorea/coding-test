import sys

p_cache = {
    0: 1,
    1: 0
}
q_cache = {
    0:0,
    1:1
}

def p(n):
    if n in p_cache:
        return p_cache[n]
    res = p(n-1) + p(n-2)
    p_cache[n] = res
    return res

def q(n):
    if n in q_cache:
        return q_cache[n]
    res = q(n-1) + q(n-2)
    q_cache[n] = res
    return res

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    print('{} {}'.format(p(N), q(N)))
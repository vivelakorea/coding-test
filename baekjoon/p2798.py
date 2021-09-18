import sys

def p2798(N, M, cards):
    res = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if cards[i] + cards[j] + cards[k] <= M:
                    res = max(res, cards[i] + cards[j] + cards[k])
    return res

N, M = map(int, sys.stdin.readline().split(' '))
cards = list(map(int, sys.stdin.readline().split(' ')))

print(p2798(N, M, cards))
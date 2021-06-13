from sys import stdin

N = int(input())
A = list(map(int, stdin.readline().split()))

res = [-1] * N
stack = []
for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        res[stack.pop()] = A[i]
    stack.append(i)

print(*res)
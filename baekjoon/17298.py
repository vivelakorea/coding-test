from sys import stdin

N = int(input())
A = list(map(int, stdin.readline().split()))

res = [-1] * N
stack = []
for i in range(N):
    if stack and A[stack[-1]] < A[i]:
        while stack and A[stack[-1]] < A[i]:
            res[stack.pop()] = A[i]
        stack.append(i)
    else:
        stack.append(i)

print(*res)
from collections import deque

N, K = map(int, input().split())

out = []

q = deque(range(1, N + 1))

while q:
  for _ in range(K-1):
    q.append(q.popleft())
  out.append(q.popleft())

print('<'+str(out)[1:-1]+'>')
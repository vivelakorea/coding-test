from collections import deque

T = int(input())

for _ in range(T):
  N, M = map(int, input().split())
  priorities = list(map(int, input().split()))
  
  q = deque()
  for i in range(N):
    q.append((i, priorities[i]))
  priorities.sort()

  res = 0
  while True:
    p = q.popleft()
    if p[1] < priorities[-1]:
      q.append(p)
    else:
      res += 1
      priorities.pop()
      if p[0] == M: 
        break
  print(res)
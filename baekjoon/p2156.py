import sys

n = int(sys.stdin.readline())
wines = [0] * n
for i in range(n):
  wines[i] = int(sys.stdin.readline())

# corner case
if n == 1:
  print(wines[0])
elif n == 2:
  print(sum(wines))

else:
  max_wines = [0] * n
  for i in range(n):
    max_wines[i] = [0,0]
  max_wines[0] = [wines[0], wines[0]]
  ans = wines[0]
  max_wines[1] = [wines[0] + wines[1], wines[1]]
  ans = wines[0]
  ans_without = wines[1]
  for i in range(2, n):
    max_wines[i][0] = ans_without + wines[i]
    max_wines[i][1] = ans + wines[i]
    ans_without = max(ans_without, max_wines[i-1][0], max_wines[i][1])
    ans = max(ans, max_wines[i-1][0], max_wines[i-1][1])
  print(max(ans, ans_without, max_wines[n-1][0], max_wines[n-1][1]))
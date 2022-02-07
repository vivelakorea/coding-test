N = int(input())

res = [] # res[0]은 의미없음
for i in range(N+1):
  res.append([0]*10) # [0으로 끝나는 경우의 수, 1로 끝나는 경우의 수, ...]

for i in range(1, 10):
  res[1][i] = 1


for i in range(2, N+1):
  res[i][0] = res[i-1][1]
  for j in range(1, 9):
    res[i][j] = (res[i-1][j-1] + res[i-1][j+1]) % 1000000000
  res[i][9] = res[i-1][8]

ans = 0
for num in res[N]:
  ans += num % 1000000000
  ans %= 1000000000

print(ans)
# input
N = int(input())
scores = [0] * N
for i in range(N):
  scores[i] = int(input())

# corner case
if N == 1:
  print(scores[0])
elif N == 2:
  print(sum(scores))
else:

  # initialization
  max_scores = [[0,0]] * N # [직전에서 한 칸으로 온 경우, 두 칸으로 온 경우]
  for i in range(N):
    max_scores[i] = [0,0]

  # dp
  max_scores[0] = [scores[0], scores[0]]
  max_scores[1] = [scores[0]+scores[1], scores[1]]

  for i in range(2, N):
    max_scores[i][0] = max_scores[i-1][1] + scores[i]
    max_scores[i][1] = max(max_scores[i-2]) + scores[i]

  print(max(max_scores[N-1]))
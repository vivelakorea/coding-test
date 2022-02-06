N = int(input())
if N == 1: print(0)
elif N == 2: print(1)
else:
  min_calcs = [0] * (N+1)
  min_calcs[2] = 1 # min_calcs[0]은 의미없음
  for i in range(3, N+1):
    possibles = []
    possibles.append(min_calcs[i-1])
    if i % 2 == 0: possibles.append(min_calcs[int(i / 2)])
    if i % 3 == 0: possibles.append(min_calcs[int(i / 3)])
    min_calcs[i] = 1 + min(possibles)

  print(min_calcs[N])
    
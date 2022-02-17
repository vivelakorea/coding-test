import sys
import heapq
heap = []
N = int(sys.stdin.readline())
for _ in range(N):
  x = int(sys.stdin.readline())
  if x == 0:
    if len(heap) == 0:
      print(0)
    else:
      print(heapq.heappop(heap))
  else:
    heapq.heappush(heap, x)
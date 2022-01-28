import sys
from collections import deque

deq = deque()

N = int(sys.stdin.readline())

for _ in range(N):
  command = sys.stdin.readline().split()
  if len(command) == 2:
    x = int(command[1])
  command = command[0]

  if command == 'push_front':
    deq.appendleft(x)
  elif command == 'push_back':
    deq.append(x)
  elif command == 'pop_front':
    print(-1 if len(deq) == 0 else deq.popleft())
  elif command == 'pop_back':
    print(-1 if len(deq) == 0 else deq.pop())
  elif command == 'size':
    print(len(deq))
  elif command == 'empty':
    print(1 if len(deq) == 0 else 0)
  elif command == 'front':
    print(-1 if len(deq) == 0 else deq[0])
  elif command == 'back':
    print(-1 if len(deq) == 0 else deq[-1])
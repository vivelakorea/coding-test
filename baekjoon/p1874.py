from collections import deque

n = int(input())
stack = []
supply = list(range(n,0,-1))
demand = deque()
for _ in range(n):
    demand.append(int(input()))

# current demand: demand[0]
# current what stack have: stack[-1]
# if current what stack have is current demand, pop it, and remove demand
# else, put new supply, supply.pop()

#stack.append(supply.pop()) # stack: [1], supply: [n,n-1,...2]
sequence = ''
while demand:
    if stack and stack[-1] == demand[0]:
        stack.pop()
        demand.popleft()
        sequence += '-\n'
    else:
        if supply:
            stack.append(supply.pop())
            sequence += '+\n'
        else:
            sequence = 'NO'
            break

print(sequence)
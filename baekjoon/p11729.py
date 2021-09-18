import sys

move = []
count = 0

def p11729(a, b, n):
    global move, count
    if n == 1:

        move.append((a, b))
        count += 1

        return

        
    p11729(a, 6-a-b, n-1)

    move.append((a, b))
    count += 1

    p11729(6-a-b, b, n-1)




N = int(sys.stdin.readline())

p11729(1, 3, N)
print(count)
for a, b in move:
    print('{} {}'.format(a, b))

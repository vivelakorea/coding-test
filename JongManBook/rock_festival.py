import sys
def rock_festival(N, n, costs):
    
    best = sys.maxsize
    
    sum_table = []
    for _ in range(N+1):
        sum_table.append([0] * (N+1))
    for i in range(N):
        sum_table[i][i+1] = costs[i]
        for j in range(i+2, N+1):
            sum_table[i][j] = sum_table[i][j-1] + costs[j-1]
    for i in range(N):
        for j in range(i+1, N+1):
            sum_table[i][j] /= (j - i)
    for i in range(N):
        for j in range(i+n, N+1):
            best = min(best, sum_table[i][j])
    return best

T = int(input())
for _ in range(T):
    N, n = map(int, input().split(' '))
    costs = list(map(int, input().split(' ')))
    print('%.11f' % (rock_festival(N, n, costs)))
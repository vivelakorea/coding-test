N, K = map(int, input().split())
coins = []
for i in range(N):
    coins.append(int(input()))
count = 0
for i in range(N-1, -1, -1):
    if K == 0:
        break
    
    count_tmp, K = divmod(K, coins[i])
    count += count_tmp

print(count)
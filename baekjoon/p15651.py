def p15651(N, M):
    permutations = []
    def dfs(M, remain, permutation):
        if M == 0:
            permutations.append(permutation[:])
            return
        for i in range(len(remain)):
            permutation.append(remain[i])
            dfs(M - 1, remain[:], permutation)
            permutation.pop()
    dfs(M, list(range(1, N+1)), list())
    return permutations

N, M = map(int, input().split(' '))
for permutation in p15651(N, M):
    for num in permutation:
        print(num, end=' ')
    print()
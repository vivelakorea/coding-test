def p7568(weight_height_pairs):
    ranks = []
    for i in range(len(weight_height_pairs)):
        # ith one's rank
        rank = 1
        for j in range(len(weight_height_pairs)):
            if i == j:
                continue
            if weight_height_pairs[j][0] > weight_height_pairs[i][0] and weight_height_pairs[j][1] > weight_height_pairs[i][1]:
                rank += 1
        ranks.append(rank)

    return ranks


N = int(input())
weight_height_pairs = []
for _ in range(N):
    weight, height = map(int, input().split(' '))
    weight_height_pairs.append((weight, height))

for rank in p7568(weight_height_pairs):
    print(rank, end=' ')
N = int(input())
RGBs = []
for i in range(N):
    RGBs.append(list(map(int, input().split())))

for i in range(1, N):
    RGBs[i][0] += min(RGBs[i-1][1], RGBs[i-1][2])
    RGBs[i][1] += min(RGBs[i-1][0], RGBs[i-1][2])
    RGBs[i][2] += min(RGBs[i-1][0], RGBs[i-1][1])

print(min(RGBs[N-1]))

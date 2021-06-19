N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

for num in sorted(arr):
    print(num)
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

def bin_search(arr, num, left, right):
  if left >= right:
    return 0

  mid = (left + right) // 2

  if arr[mid] == num:
    return 1
  elif arr[mid] < num:
    return bin_search(arr, num, mid+1, right)
  else:
    return bin_search(arr, num, left, mid)
  

A.sort()
for b in B:
  print(bin_search(A, b, 0, N))
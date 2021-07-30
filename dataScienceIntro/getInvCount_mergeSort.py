import random

def getInvCount(arr, n):
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                inv_count += 1
    return inv_count

def getInvCount_mergeSort(arr, n):
    if n == 1:
        return arr, 0
    (B, x) = getInvCount_mergeSort(arr[:n // 2] , n // 2)
    (C, y) = getInvCount_mergeSort(arr[n // 2:], n // 2 + n % 2)
    (D, z) = Merge_and_CountSplitInv(B, C)
    
    return D, x + y + z


def Merge_and_CountSplitInv(arr1, arr2):
    merged = []
    p1, p2 = 0, 0
    count = 0
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            merged.append(arr1[p1])
            p1 += 1
        else:
            merged.append(arr2[p2])
            p2 += 1
            count += len(arr1) - p1
    if p1 == len(arr1):
        while p2 < len(arr2):
            merged.append(arr2[p2])
            p2 += 1 
    else:
        while p1 < len(arr1):
            merged.append(arr1[p1])
            p1 += 1

    return merged, count


testCases = []
for _ in range(10):
    testCase = list(range(100))
    random.shuffle(testCase)
    testCases.append(testCase)
    
for testCase in testCases:
    print(getInvCount(testCase, len(testCase)), getInvCount_mergeSort(testCase, len(testCase))[1])
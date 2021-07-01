# Function to Use Inversion Count
def getInvCount_mergeSort(arr, n):

    # Fill in this space
    # Hint: you can use the merge-sort code from yesterday's session
    if n == 1:
        return arr, 0
    (B, x) = getInvCount_mergeSort(arr[:n // 2] , n // 2)
    (C, y) = getInvCount_mergeSort(arr[n // 2:], n // 2 + n % 2)
    (D, z) = Merge_and_CountSplitInv(B, C, n)
    
    return D, x + y + z# what should you return?


def Merge_and_CountSplitInv(arr1, arr2, n):
    # print('arr1', arr1, 'arr2', arr2)
    merged = []
    p1, p2 = 0, 0
    count = 0
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            merged.append(arr1[p1])
            # print('merging...', merged)
            p1 += 1
        else:
            merged.append(arr2[p2])
            # print('merging...', merged)
            p2 += 1
            # print('count!')
            count += len(arr1) - p1
    if p1 == len(arr1):
        while p2 < len(arr2):
            merged.append(arr2[p2])
            # print('merging...', merged)
            p2 += 1 
    else:
        while p1 < len(arr1):
            merged.append(arr1[p1])
            # print('merging...', merged)
            p1 += 1
        
    # print('merged', merged, 'count', count)
            
    return merged, count
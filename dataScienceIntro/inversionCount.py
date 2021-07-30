from typing import List
import random

class Solution:
    def getInvCount_mergeSort(self, arr: List[int]):

        n = len(arr)
        if n == 1:
            return arr, 0
        B, x = self.getInvCount_mergeSort(arr[:n // 2])
        C, y = self.getInvCount_mergeSort(arr[n // 2:])
        D, z = self.Merge_and_CountSplitInv(B, C)
        
        return D, x + y + z


    def Merge_and_CountSplitInv(self, arr1: List[int], arr2: List[int]):

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


    def getInvCount(self, arr):

        n = len(arr)
        inv_count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (arr[i] > arr[j]):
                    inv_count += 1

        return inv_count

s = Solution()

testCases = []
for _ in range(10):
    testCase = list(range(10000))
    random.shuffle(testCase)
    testCases.append(testCase)

for testCase in testCases:
    print(s.getInvCount(testCase), s.getInvCount_mergeSort(testCase)[1])

f = open('nums.txt', 'r')
nums = list(map(int, f.readlines()))
# print(s.getInvCount(nums))
print(s.getInvCount(nums), s.getInvCount_mergeSort(nums)[1])
f.close()
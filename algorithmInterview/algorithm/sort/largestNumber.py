from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def merge(arr1: List, arr2: List) -> List:
            merged = []
            p1, p2 = 0, 0
            while p1 < len(arr1) and p2 < len(arr2):
                if int(str(arr1[p1]) + str(arr2[p2])) > int(str(arr2[p2]) + str(arr1[p1])):
                    merged.append(arr1[p1])
                    p1 += 1
                else:
                    merged.append(arr2[p2])
                    p2 += 1
            if p1 == len(arr1):
                while p2 < len(arr2):
                    merged.append(arr2[p2])
                    p2 +=1 
            else:
                while p1 < len(arr1):
                    merged.append(arr1[p1])
                    p1 +=1 
            return merged

        def mergeSort(arr) -> List:
            if len(arr) <= 1:
                return arr
            arr1 = mergeSort(arr[:len(arr) // 2])
            arr2 = mergeSort(arr[len(arr) // 2:])
            return merge(arr1, arr2)

        return str(int(''.join([str(n) for n in mergeSort(nums)])))


s = Solution()
print(s.largestNumber([1]))
print(s.largestNumber([10, 2]))
print(s.largestNumber([3, 30, 34, 5, 9]))
print(s.largestNumber([10]))
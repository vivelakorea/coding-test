from typing import List
import random

class Sort:
    def __init__(self, arr: List):
        self.arr = arr

    def __str__(self):
        s = ''
        s += 'before sort:\t{}\n'.format(self.arr)
        s += 'bubble sort:\t{}\n\n'.format(self.bubbleSort(self.arr))
        self.mix()
        s += 'before sort:\t{}\n'.format(self.arr)
        s += 'merge sort:\t{}\n\n'.format(self.mergeSort(self.arr))
        self.mix()
        s += 'before sort:\t{}\n'.format(self.arr)
        s += 'quick sort:\t{}\n\n'.format(self.quickSort(self.arr, 0, len(self.arr) - 1))
        self.mix()
        s += 'before sort:\t{}\n'.format(self.arr)
        s += 'insertion sort:\t{}\n\n'.format(self.insertionSort(self.arr))
        
        return s
        
    def mix(self):
        random.shuffle(self.arr)

    def bubbleSort(self, arr: List) -> List:
        for i in range(len(arr)-1):
            for j in range(len(arr)-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    
    def merge(self, arr1: List, arr2: List) -> List:
            merged = []
            p1, p2 = 0, 0
            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1] < arr2[p2]:
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

    def mergeSort(self, arr) -> List:
        if len(arr) <= 1:
            return arr
        arr1 = self.mergeSort(arr[:len(arr) // 2])
        arr2 = self.mergeSort(arr[len(arr) // 2:])
        return self.merge(arr1, arr2)

    def partition(self, arr, left, right):
        p = right
        right = p - 1
        while left <= right:
            if arr[left] < arr[p]:
                left += 1
            elif arr[right] > arr[p]:
                right -= 1
            else:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        arr[p], arr[left] = arr[left], arr[p]
        p = left
        return p
    
    def quickSort(self, arr, left, right):
        if left < right:
            p = self.partition(arr, left, right)
            self.quickSort(arr, left, p - 1)
            self.quickSort(arr, p + 1, right)
        return arr

    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            j = 0
            while arr[i] > arr[j]:
                j += 1
            tmp = arr[i]
            arr[j + 1:i + 1] = arr[j:i]
            arr[j] = tmp
        return arr

for i in range(10):
    arr = [j for j in range(i)] + [j for j in range(i // 2)]
    random.shuffle(arr)
    s = Sort(arr)
    print(s)
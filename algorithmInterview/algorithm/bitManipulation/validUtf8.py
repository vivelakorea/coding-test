from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(arr, i, j):
            for k in range(i + 1, i + j + 1):
                if k >= len(arr) or (arr[k] >> 6) != 0b10:
                    return False
            return True
        
        i = 0
        while i < len(data):
            if (data[i] >> 3) == 0b11110 and check(data, i, 3):
                i += 4
            elif (data[i] >> 4) == 0b1110 and check(data, i, 2):
                i += 3
            elif (data[i] >> 5) == 0b110 and check(data, i, 1):
                i += 2
            elif (data[i] >> 7) == 0b0:
                i += 1
            else:
                return False

        return True


s = Solution()
print(s.validUtf8([197,130,1]))
print(s.validUtf8([235,140,4]))
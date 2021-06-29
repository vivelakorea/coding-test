from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        N = len(mat)
        M = len(mat[0])
        def find(row_top, row_bottom, column_left, column_right):
            row_mid = (row_top + row_bottom) // 2
            column_mid = (column_left + column_right) // 2

            if row_mid + 1 < N and mat[row_mid][column_mid] < mat[row_mid + 1][column_mid]:
                return find(row_mid + 1, row_bottom, colmun_left, column_right)
            elif row_mid - 1 >= 0 and mat[row_mid][column_mid] < mat[row_mid - 1][column_mid]:
                return find(row_top, row_mid, column_left, column_right)
            elif column_mid + 1 < M and mat[row_mid][column_mid] < mat[row_mid][column_mid + 1]:
                return find(row_top, row_bottom, column_mid + 1, column_right)
            elif column_mid - 1 >= 0 and mat[row_mid][column_mid] < mat[row_mid][column_mid - 1]:
                return find(row_top, row_bottom, colmun_left, column_mid)
            else:
                return [row_mid, column_mid]
        return find(0, N, 0, M)

s = Solution()
print(s.findPeakGrid([[1,4],[3,2]]))
print(s.findPeakGrid([[10,20,15],[21,30,14],[7,16,32]]))
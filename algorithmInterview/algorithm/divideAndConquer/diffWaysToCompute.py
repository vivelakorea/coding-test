# https://leetcode.com/problems/different-ways-to-add-parentheses/

from itertools import product
from typing import List

class Solution:
    def diffWaysToCompute__helper(self, expression: str) -> List[int]:
        borders = []
        for i in range(len(expression)):
            if expression[i] in ['+', '-', '*']:
                borders.append(i)
                
        # base case
        if len(borders) == 0:
            return [int(expression)]
        
        res = []
        for border in borders:
            # divide
            left = self.diffWaysToCompute__helper(expression[:border])
            right = self.diffWaysToCompute__helper(expression[border + 1:])
            # conquer
            if expression[border] == '+':
                res.extend([x + y for x, y in product(left, right)])
            elif expression[border] == '-':
                res.extend([x - y for x, y in product(left, right)])
            else:
                res.extend([x * y for x, y in product(left, right)])
        return res
    
    def diffWaysToCompute(self, expression: str) -> List[int]:
        return self.diffWaysToCompute__helper(expression)

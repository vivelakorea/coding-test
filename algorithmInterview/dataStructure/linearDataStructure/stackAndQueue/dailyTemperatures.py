from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                popped = stack.pop()
                res[popped] = i - popped
            stack.append(i)
        
        return res

s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
print(s.dailyTemperatures([30,40,50,60]))
print(s.dailyTemperatures([30,60,90]))
print(s.dailyTemperatures([31,32,33,34,35,36]))
print(s.dailyTemperatures([35,32,33,34,35,36]))
print(s.dailyTemperatures([30]))
print(s.dailyTemperatures([100]))
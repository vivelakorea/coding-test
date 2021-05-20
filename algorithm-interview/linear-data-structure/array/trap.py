import collections
class Solution:
    def trap(self, height) -> int:
        stack =  []
        traped = 0
        for i in range(len(height)):
            while stack and stack[-1][1] <= height[i]:
                blocked = stack.pop()
                traped += (i - blocked[0] - 1) * (blocked[1] - blocked[2])
            if ( i != len(height) - 1 ) and ( height[i] > height[i + 1] ):
                stack.append([i, height[i], 0])
            else:
                for bar in stack:
                    bar[2] = max(bar[2], height[i])
        return traped


s = Solution()
print(s.trap([4,2,0,3,2,5]))
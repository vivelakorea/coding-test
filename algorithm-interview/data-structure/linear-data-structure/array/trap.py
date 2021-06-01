import collections
class Solution:
    def trap1(self, height) -> int:
        # two pointer
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[0], height[-1]
        trapped = 0
        while left < right:
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                if height[left] < left_max:
                    trapped += left_max - height[left]
            else: # left_max > right_max
                right -= 1
                right_max = max(right_max, height[right])
                if height[right] < right_max:
                    trapped += right_max - height[right]
        return trapped
        
    def trap2(self, height) -> int:
        # stack
        stack = []
        trapped = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                popped = stack.pop()
                if not stack:
                    break
                h = min(height[i], height[stack[-1]]) - height[popped]
                w = i - stack[-1] - 1
                trapped += h * w
            stack.append(i)
        return trapped


s = Solution()
print(s.trap1([4,2,0,3,2,5]))
print(s.trap2([4,2,0,3,2,5]))

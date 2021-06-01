import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        queue = collections.deque()
        if root: # root가 None인 경우 21번줄에서 오류 날 수 있기 때문에 다는 조건
            queue.append([root])
        while queue:
            depth += 1
            nodes = queue.popleft()
            children = []
            for node in nodes:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            if children:
                queue.append(children)
        return depth

r = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
s = Solution()
print(s.maxDepth(r))
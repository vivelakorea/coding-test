import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ### bft
        # depth = 0
        # queue = collections.deque()
        # if root: # root가 None인 경우 21번줄에서 오류 날 수 있기 때문에 다는 조건
        #     queue.append([root])
        # while queue:
        #     depth += 1
        #     nodes = queue.popleft()
        #     children = []
        #     for node in nodes:
        #         if node.left:
        #             children.append(node.left)
        #         if node.right:
        #             children.append(node.right)
        #     if children:
        #         queue.append(children)
        # return depth

        ### dft by stack

        ## preorder
        # if not root:
        #     return 0
        # maxDepth = 1
        # stack = [(root, 1)]
        # while stack:
        #     node, depth = stack.pop()
        #     maxDepth = max(maxDepth, depth)
        #     depth += 1
        #     if node.left:
        #         stack.append((node.left, depth))
        #     if node.right:
        #         stack.append((node.right, depth))
        # return maxDepth

        ## indorder
        if not root:
            return 0
        maxDepth = 1
        stack = []
        cur = (root, 1)
        while True:
            print(cur[0].val if cur[0] else None, cur[1])
            while cur[0]:
                stack.append(cur)
                cur = (cur[0].left, cur[1] + 1)
            cur = stack.pop()
            if not cur[0]:
                break
            maxDepth = max(maxDepth, cur[1])
            cur = (cur[0].right, cur[1] + 1)
        return maxDepth

            
            

r = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
s = Solution()
print(s.maxDepth(r))
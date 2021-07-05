# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        
        def convert(arr):
            if len(arr) == 0:
                return None
            if len(arr) == 1:
                return TreeNode(arr[0])
            mid = len(arr) // 2
            root = TreeNode(arr[mid])
            root.left = convert(arr[:mid])
            root.right = convert(arr[mid+1:])
            return root
        
        return convert(arr)

s = Solution()
print(s.sortedListToBST(ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))))
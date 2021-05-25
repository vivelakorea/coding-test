# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast, slow = head, head
        stack = [slow.val]
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            stack.append(slow.val)
        if fast.next == None: 
            stack.pop()
        while slow.next:
            slow = slow.next
            if stack.pop() != slow.val:
                return False
        return True

s = Solution()
print(s.isPalindrome(ListNode(1,ListNode(2, ListNode(1)))))

        
            

            
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l2.val <= l1.val:
            root = cur = l2
            side = l1
        else:
            root = cur = l1
            side = l2
        
        while cur and cur.next and side:
            if cur.next.val <= side.val:
                cur = cur.next
            else:
                tmp = side
                side = cur.next
                cur.next = tmp
                cur = cur.next

        cur.next = side
        
        return root


def list_to_linked_list(l):
    if not l:
        return ListNode()
    root = cur = ListNode(l[0])
    for i in range(1, len(l)):
        cur.next = ListNode(l[i])
        cur = cur.next
    return root

s = Solution()

ll1 = list_to_linked_list([1,3,5,7,9,11])
ll2 = list_to_linked_list([-10,20])

print(s.mergeTwoLists(ll1, ll2))
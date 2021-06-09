import os, sys
cur_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(cur_dir)))

from dataStructure.linearDataStructure.linkedList.linked_list import ListNode, list_to_linked_list

class Solution:
    def merge(self, head1: ListNode, head2: ListNode):
        root = merged = ListNode(None)
        while head1 and head2:
            if head1.val < head2.val:
                merged.next = ListNode(head1.val)
                head1 = head1.next
                merged = merged.next
            else:
                merged.next = ListNode(head2.val)
                head2 = head2.next
                merged = merged.next
        if head1:
            merged.next = head1
        else:
            merged.next = head2
        return root.next

    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        head1, slow, fast = head, head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        slow.next = None
        return self.merge(self.sortList(head1), self.sortList(head2))

        
        

s = Solution()
print(s.merge(list_to_linked_list([1,2,3]), list_to_linked_list([2,3,5])))
print(s.sortList(list_to_linked_list([])))
print(s.sortList(list_to_linked_list([3])))
print(s.sortList(list_to_linked_list([4,2])))
print(s.sortList(list_to_linked_list([4,2,1])))
print(s.sortList(list_to_linked_list([4,2,1,3])))
print(s.sortList(list_to_linked_list([4,2,1,3,5])))
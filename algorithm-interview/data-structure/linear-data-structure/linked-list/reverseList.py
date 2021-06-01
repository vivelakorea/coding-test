from linked_list import ListNode, list_to_linked_list

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        dummy_head = ListNode(None, head)
        a, b, root = dummy_head, head, head

        while b:
            c = b.next
            b.next = a
            a = b
            b = c
        
        root.next = None

        return a

s = Solution()
print(s.reverseList(list_to_linked_list([1,2,3])))
print(s.reverseList(list_to_linked_list([])))
print(s.reverseList(list_to_linked_list([1])))
print(s.reverseList(list_to_linked_list([1,2])))


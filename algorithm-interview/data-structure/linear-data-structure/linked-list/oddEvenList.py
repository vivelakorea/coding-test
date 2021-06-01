from linked_list import ListNode, list_to_linked_list

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        a, odd_start, b, even_start = head, head, head.next, head.next

        while b and b.next:
            tmp = b.next
            a.next = b.next
            b.next = b.next.next
            a = tmp
            b = tmp.next

        a.next = even_start
        return odd_start
        

s = Solution()
print(s.oddEvenList(list_to_linked_list([])))
print(s.oddEvenList(list_to_linked_list([1])))
print(s.oddEvenList(list_to_linked_list([1,2])))
print(s.oddEvenList(list_to_linked_list([1,2,3])))
print(s.oddEvenList(list_to_linked_list([1,2,3,4])))
print(s.oddEvenList(list_to_linked_list([1,2,3,4,5])))
print(s.oddEvenList(list_to_linked_list([1,2,3,4,5,6])))

from linked_list import ListNode, list_to_linked_list

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head

        a = d = ListNode(None, head)
        i = 0

        while i < left - 1:
            a = a.next
            i += 1
        prev = a
        start = a = a.next
        i += 1
        b = a.next
        
        while i < right:
            tmp = b.next
            b.next = a
            a = b
            i += 1
            b = tmp
        
        prev.next = a
        start.next = b

        return d.next



s = Solution()
print(s.reverseBetween(list_to_linked_list([1]), 1, 1)) # [1]
print(s.reverseBetween(list_to_linked_list([1, 2]), 1, 1)) # [1, 2]
print(s.reverseBetween(list_to_linked_list([1, 2]), 1, 2)) # [2, 1]
print(s.reverseBetween(list_to_linked_list([1, 2]), 2, 2)) # [1, 2]
print(s.reverseBetween(list_to_linked_list([1, 2, 3]), 1, 1)) # [1, 2, 3]
print(s.reverseBetween(list_to_linked_list([1, 2, 3]), 1, 2)) # [2, 1, 3]
print(s.reverseBetween(list_to_linked_list([1, 2, 3]), 1, 3)) # [3, 2, 1]
print(s.reverseBetween(list_to_linked_list([1, 2, 3]), 2, 3)) # [1, 3, 2]
print(s.reverseBetween(list_to_linked_list([1, 2, 3]), 3, 3)) # [1, 2, 3]
print(s.reverseBetween(list_to_linked_list([1, 2, 3, 4]), 2, 3)) # [1, 3, 2, 4]
print(s.reverseBetween(list_to_linked_list([1, 2, 3, 4, 5]), 2, 4)) # [1, 4, 3, 2, 5]
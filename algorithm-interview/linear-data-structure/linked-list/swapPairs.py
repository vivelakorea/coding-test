from linked_list import ListNode, list_to_linked_list

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        d2 = ListNode(None, head)
        d1 = ListNode(None, d2)
        a, b = d1, head

        while b and b.next:
            tmp = b.next.next
            a.next = b.next
            b.next.next = b
            a = b
            b = tmp

        a.next = b


        return d1.next
s = Solution()
print(s.swapPairs(list_to_linked_list([])))
print(s.swapPairs(list_to_linked_list([1])))
print(s.swapPairs(list_to_linked_list([1,2])))
print(s.swapPairs(list_to_linked_list([1,2,3])))
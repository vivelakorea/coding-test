from linked_list import ListNode, list_to_linked_list

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_node = cur = ListNode()
        carry = 0
        while l1 and l2:
            cur.next = ListNode()
            cur = cur.next
            val = l1.val + l2.val + carry
            carry, val = divmod(val, 10)
            cur.val = val
            l1, l2 = l1.next, l2.next
        
        if not (l1 or l2):
            if carry:
                cur.next = ListNode(carry)
            return dummy_node.next

        if l1:
            while l1:
                cur.next = ListNode()
                cur = cur.next
                val = l1.val + carry
                carry, val = divmod(val, 10)
                cur.val = val
                l1 = l1.next
            if carry:
                cur.next = ListNode(carry)
            return dummy_node.next

        if l2:
            while l2:
                cur.next = ListNode()
                cur = cur.next
                val = l2.val + carry
                carry, val = divmod(val, 10)
                cur.val = val
                l2 = l2.next
            if carry:
                cur.next = ListNode(carry)
            return dummy_node.next


s = Solution()
print(s.addTwoNumbers(
    list_to_linked_list([2,4,6]),
    list_to_linked_list([5,6,4])))
print(s.addTwoNumbers(
    list_to_linked_list([2,4]),
    list_to_linked_list([5,6,9])))
print(s.addTwoNumbers(
    list_to_linked_list([2,4,9]),
    list_to_linked_list([5,6])))
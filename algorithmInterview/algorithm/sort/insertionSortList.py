import os, sys
cur_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(cur_dir)))

from dataStructure.linearDataStructure.linkedList.linked_list import ListNode, list_to_linked_list

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(None, head)
        p1_prev, p1 = dummy, dummy.next
        tmp_prev = tmp = None
        while p1.next:
            if tmp:
                p1_prev, p1 = tmp_prev, tmp
            else:
                p1_prev, p1 = p1, p1.next
            p2_prev, p2 = dummy, dummy.next
            # print('p1_prev.val:',p1_prev.val, 'p1.val:', p1.val)
            while p1 != p2 and p1.val >= p2.val:
                p2_prev, p2 = p2, p2.next
            if p1 != p2:
                tmp_prev, tmp = p1_prev, p1.next
                p2_prev.next = p1
                p1_prev.next = p1.next
                p1.next = p2
            else:
                tmp = None
            # print('nodes:', dummy.next)
        return dummy.next
        


# head = ListNode(1, ListNode(1, ListNode(3)))
# p1 = head.next
# p2 = head

# print(p1 == p2)
# p2 = p2.next
# print(p1 == p2)


s = Solution()
print(s.insertionSortList(list_to_linked_list([1])))
print(s.insertionSortList(list_to_linked_list([1,2])))
print(s.insertionSortList(list_to_linked_list([2,1])))
print(s.insertionSortList(list_to_linked_list([4,2,1,3])))
print(s.insertionSortList(list_to_linked_list([-1,5,3,4,0])))
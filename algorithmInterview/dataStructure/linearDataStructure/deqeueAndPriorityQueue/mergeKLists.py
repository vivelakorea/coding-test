from typing import List
import os, sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from linkedList.linked_list import ListNode, list_to_linked_list

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ## node 전체를 복사하지 않고 값만 복사해오는 야매 풀이
        # import heapq
        # h = []
        # for l in lists:
        #     while l:
        #         heapq.heappush(h, l.val)
        #         l = l.next
        # root = res = ListNode(None)
        # while h:
        #     res.next = ListNode(None)
        #     res = res.next
        #     res.val = heapq.heappop(h)
        # return root.next
        import heapq
        h = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(h, (l.val, i, l)) # l 자체는 비교연산이 안되기 때문에 그 앞에 무조건 같지 않은 대소관계가 있는 i를 넣어줘야 함
        root = res = ListNode(None)
        while h:
            _, idx, node = heapq.heappop(h)
            res.next = node
            res = res.next
            if node.next:
                heapq.heappush(h, (node.next.val, idx, node.next))
        return root.next

s = Solution()
print(s.mergeKLists([

]))
print(s.mergeKLists([
    None
]))
print(s.mergeKLists([
    list_to_linked_list([1,4,5])
]))
print(s.mergeKLists([
    list_to_linked_list([1,4,5]),
    list_to_linked_list([2,6])
]))
print(s.mergeKLists([
    list_to_linked_list([1,4,5]),
    list_to_linked_list([1,3,4]),
    list_to_linked_list([24,32,62]),
    list_to_linked_list([2,6,44,52]),
    list_to_linked_list([1,3,6,10,3,4,3])
]))

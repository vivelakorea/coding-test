# https://leetcode.com/problems/queue-reconstruction-by-height/

from typing import List

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
    def toList(self):
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        root = cur = ListNode(None)
        for person in people:
            # print('person', person)
            cur = root
            for _ in range(person[1]):
                cur = cur.next
                # print('cur', cur.val)
            tmp = cur.next
            cur.next = ListNode(person, tmp)
            # print('root', root)
        return root.next.toList()

s = Solution()
print(s.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
        
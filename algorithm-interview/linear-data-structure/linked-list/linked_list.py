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


def list_to_linked_list(l):
    if not l:
        return None
    root = cur = ListNode(l[0])
    for i in range(1, len(l)):
        cur.next = ListNode(l[i])
        cur = cur.next
    return root
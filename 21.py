# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            if l2 is None:
                return None
            else:
                return l2
        elif l2 is None:
            return l1

        c1, c2 = l1, l2
        if c1.val < c2.val:
            ret = ListNode(c1.val)
            c1 = c1.next
        else:
            ret = ListNode(c2.val)
            c2 = c2.next
        rc = ret
        while c1 is not None or c2 is not None:
            if c1 is None:
                while c2 is not None:
                    rc.next = ListNode(c2.val)
                    c2 = c2.next
                    rc = rc.next
                break

            if c2 is None:
                while c1 is not None:
                    rc.next = ListNode(c1.val)
                    c1 = c1.next
                    rc = rc.next
                break

            if c1.val < c2.val:
                rc.next = ListNode(c1.val)
                c1 = c1.next
            else:
                rc.next = ListNode(c2.val)
                c2 = c2.next
            rc = rc.next

        return ret

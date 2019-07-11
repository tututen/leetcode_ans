from typing import List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        c = head
        it = head
        while it.next != None:
            it = it.next
            if c.val == it.val:
                continue
            else:
                c.next = it
                c = it
        else:
            if c.val == it.val:
                c.next = None
        return head

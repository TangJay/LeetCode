# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
        ans = head.next
        a = head
        b = a.next
        c = b.next
        if c != None:
            d = c.next
        else:
            d = None
        while True:
            b.next = a
            if d == None:
                a.next = c
                break
            a.next = d
            a = c
            b = d
            c = b.next
            if c == None:
                d = None
            else:
                d = c.next
        return ans

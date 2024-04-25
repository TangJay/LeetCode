# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        add = copy.deepcopy(head)
        head = ListNode(val = 0, next = add)
        begin = head
        while True:
            self.start = begin
            for i in range(k):
                if self.start == None:
                    break
                self.start = self.start.next
            if self.start == None:
                break
            self.start = begin.next
            begin.next = self.reverse(k)
            for i in range(k):
                begin = begin.next
        return head.next
    def reverse(self, times): 
        start = self.start
        master = start
        Next = start.next
        end = start
        for i in range(times):
            end = end.next
        master.next = end
        for i in range(times - 1):
            start = Next
            Next = start.next
            start.next = master
            master = start
        return master


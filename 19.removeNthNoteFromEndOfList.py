# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        item = head
        number = 0
        while item != None:
            number += 1
            item = item.next
        item = head
        for i in range(number - n):
            master = item
            item = item.next
        if number == 1:
            return 
        elif n == 1:
            master.next = None
            return head
        item.val = item.next.val
        item.next = item.next.next
        return head

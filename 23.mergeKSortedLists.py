# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        self.nums = []
        for i in lists:
            self.open(i)
        self.nums.sort()
        if len(self.nums) == 0:
            return 
        ans = ListNode()
        now = ans
        for i in range(len(self.nums)):
            now.val = self.nums[i]
            if i != len(self.nums) - 1:
                now.next = ListNode()
                now = now.next
        now = None
        return ans
    def open(self, L):
        while L != None:
            self.nums.append(L.val)
            L = L.next
        return
            
        
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        num = 0
        mark = []
        for i in range(len(nums)):
            if nums[i] == val:
                num += 1
                mark.append(i)
        mark.reverse()
        for i in mark:
            nums.pop(i)
        for i in range(num):
            nums.append(0)
        return length - num
        
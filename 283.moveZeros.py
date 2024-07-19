class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in nums: 
            if i == 0:
                nums.remove(0)
                nums.insert(len(nums), 0)
        """
        Do not return anything, modify nums in-place instead.
        """
        
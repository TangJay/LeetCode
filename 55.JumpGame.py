class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums:
            return True
        maximum = 0
        for i in range(len(nums)):
            if i == len(nums) - 1:
                return True
            if nums[i] == 0 and maximum <= i:
                return False
            if i + nums[i] > maximum:
                maximum = i + nums[i]

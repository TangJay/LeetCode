class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        ans = []
        ans.append(nums.index(target))
        nums.reverse()
        ans.append(len(nums) - nums.index(target) - 1)
        return ans
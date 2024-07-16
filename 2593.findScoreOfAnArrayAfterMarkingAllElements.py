import copy
class Solution:
    def findScore(self, nums: List[int]) -> int:
        ans = 0
        numsC = copy.deepcopy(nums)
        order = sorted(range(len(numsC)), key=lambda k: numsC[k])
        for i in order:
            if nums[i] == 1000001:
                continue
            ans += nums[i]
            if i + 1 < len(nums):
                nums[i + 1] = 1000001
            if i - 1 >= 0:
                nums[i - 1] = 1000001
            nums[i] = 1000001
        return ans
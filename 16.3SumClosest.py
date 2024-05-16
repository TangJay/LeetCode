class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 999999
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left != right:
                total = sum([nums[i], nums[left], nums[right]])
                if abs(ans - target) > abs(total - target):
                    ans = total
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                elif total == target:
                    return target
        return ans

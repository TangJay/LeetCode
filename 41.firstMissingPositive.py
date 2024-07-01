class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        print(nums, "fhj")
        nums = set(nums)
        nums = sorted(nums)
        negative = []
        for i in nums:
            if i > 0:
                break
            negative.append(i)
        for i in negative:
            nums.remove(i)
        last = 0
        for i in nums:
            if i != last + 1 and i > 0:
                return last + 1
            last = i
        return last + 1
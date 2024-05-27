class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        compare = [len(nums) - 1]
        for i in range(len(nums) - 1, -1, -1):
            for j in compare:
                if nums[j] > nums[i]:
                    temp = nums[i:]
                    temp.remove(nums[j])
                    nums[i] = nums[j]
                    del nums[i + 1 : ]
                    temp.sort()
                    for k in temp:
                        nums.append(k)
                    return
            compare.append(i - 1)
        nums.sort()
        """
        Do not return anything, modify nums in-place instead.
        """
        
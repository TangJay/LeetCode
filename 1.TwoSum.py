class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    return ans


if __name__ == "__main__":
    obj = Solution()
    ans = obj.twoSum([int(i) for i in input().split()], int(input()))
    print(ans)

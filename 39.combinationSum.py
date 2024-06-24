import copy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        candidates.sort()
        self.target = target
        self.ans = []
        for i in candidates:
            self.choose(i, i, [])
        return self.ans
    def choose(self, num, Sum, nums):
        nums.append(num)
        temp = self.candidates[self.candidates.index(num) : ]
        if Sum == self.target:
            self.ans.append(nums)
        for i in temp:
            if Sum + i < self.target:
                numC = copy.deepcopy(nums)
                self.choose(i, Sum + i, numC)
            elif Sum + i == self.target:
                nums.append(i)
                self.ans.append(nums)
                break
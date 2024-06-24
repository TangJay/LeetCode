import copy
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.target = target
        self.ans = []
        for i in set(candidates):
            candidatesC = copy.deepcopy(candidates)
            self.choose(i, i, [], candidatesC)
        temp = []
        for i in self.ans:
            if i not in temp:
                temp.append(i)
        return temp
    def choose(self, num, Sum, nums, candidates):
        temp = candidates[candidates.index(num) : ]
        candidates.remove(num)
        temp.remove(num)
        nums.append(num)
        if Sum == self.target:
            self.ans.append(nums)
        for i in set(temp):
            if Sum + i < self.target:
                numC = copy.deepcopy(nums)
                candidatesC = copy.deepcopy(candidates)
                self.choose(i, Sum + i, numC, candidatesC)
            elif Sum + i == self.target:
                nums.append(i)
                self.ans.append(nums)
                break
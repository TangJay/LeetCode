class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.nums = nums
        self.sets = []
        self.finalSet = []
        zeros = 0
        lowest = self.nums[0] + self.nums[1]
        highest = self.nums[len(self.nums) - 1] + self.nums[len(self.nums) - 2]
        if lowest * -1 < highest:
            for i in range(len(self.nums)):
                if lowest * -1 < self.nums[i]:
                    del self.nums[i : ]
                    break
        else:
            for i in range(len(self.nums)):
                if highest * -1 > self.nums[i]:
                    del self.nums[ : i + 1]
                    break
        last = None
        for i in range(len(self.nums) - 2):
            if self.nums[i] == last:
                continue
            last = self.nums[i]
            self.findSet(i)
        return self.sets
    def findSet(self, central):
        left = central + 1
        right = len(self.nums) - 1
        while right != left:
            total = sum([self.nums[central], self.nums[left], self.nums[right]])
            if total == 0:
                self.sets.append([self.nums[central], self.nums[left], self.nums[right]])
                if right - left > 2:
                    left += 1
                    right -= 1
                else:
                    break
            elif total > 0:
                right -= 1
            else:
                left += 1
            if left != central + 1:
                while self.nums[left] == self.nums[left - 1] and right - left > 1:
                    left += 1
            if right != len(self.nums) - 1:
                while self.nums[right] == self.nums[right + 1] and right - left > 1:
                    right -= 1
            
            

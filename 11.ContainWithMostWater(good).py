import copy


class Solution:
    def maxArea(self, height: List[int]) -> int:
        self.height = height
        self.left = 0
        self.right = len(height) - 1
        self.current = self.calculate()
        while self.left != self.right:
            self.compare()
        return self.current

    def compare(self):
        if self.height[self.left] < self.height[self.right]:
            self.left += 1
        else:
            self.right -= 1
        size = self.calculate()
        if size >= self.current:
            self.current = size

    def calculate(self):
        return abs(self.left - self.right) * min(
            self.height[self.right], self.height[self.left]
        )

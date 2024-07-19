class Solution:
    def trap(self, height: List[int]) -> int:
        self.ans = 0
        self.height = height
        for i in range(1, max(height) + 1):
            self.count(i)
        return self.ans
    def count(self, H):
        ables = []
        ends = []
        for i in range(len(self.height) - 1):
            if self.height[i] >= H and self.height[i + 1] < H:
                ables.append(i)
            if self.height[i] < H and self.height[i + 1] >= H and len(ends) < len(ables):
                ends.append(i + 1)
        for i in range(len(ends)):
            self.ans += ends[i] - ables[i] - 1
        
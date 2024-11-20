import copy


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.lowest = []
        temp = [None] * len(grid[0])
        for i in range(len(grid)):
            self.lowest.append(copy.deepcopy(temp))
        self.lowest[0][0] = grid[0][0]
        ans = self.calculate(len(grid) - 1, len(grid[0]) - 1)
        return ans

    def calculate(self, x, y):
        if x < 0 or y < 0:
            return float("inf")
        low = self.lowest[x][y]
        if low != None:
            return low
        else:
            low = (
                min(self.calculate(x - 1, y), self.calculate(x, y - 1))
                + self.grid[x][y]
            )
            self.lowest[x][y] = low
            return low

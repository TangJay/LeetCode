class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.X = len(obstacleGrid)
        self.Y = len(obstacleGrid[0])
        self.grid = []
        for i in range(self.X):
            self.grid.append([])
            for j in range(self.Y):
                self.grid[i].append(None)
        self.grid[0][0] = 1
        for i in range(self.X):
            for j in range(self.Y):
                if obstacleGrid[i][j] == 1:
                    self.grid[i][j] = 0
        ans = self.find(self.X - 1, self.Y - 1)
        return ans

    def find(self, targetX, targetY):
        if targetX < 0 or targetX > self.X - 1:
            return 0
        if targetY < 0 or targetY > self.Y - 1:
            return 0
        if self.grid[targetX][targetY] != None:
            return self.grid[targetX][targetY]
        ans = self.find(targetX - 1, targetY) + self.find(targetX, targetY - 1)
        self.grid[targetX][targetY] = ans
        return ans

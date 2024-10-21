class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.X = m
        self.Y = n
        self.grid = []
        for i in range(m):
            self.grid.append([])
            for j in range(n):
                self.grid[i].append(None)
        self.grid[0][0] = 1
        ans = self.find(m - 1, n - 1)
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

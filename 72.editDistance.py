import copy
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        self.chart = []
        self.word1 = " " + word1
        self.word2 = " " + word2
        for i in range(len(word2) + 1):
            self.chart.append([None] * (len(word1) + 1))
        self.chart[0][0] = 0
        if word1[0] == word2[0]:
            self.chart[0][0] = 0
        ans = self.getValue(len(word2), len(word1))
        return ans
    def getValue(self, x, y):
        if x < 0 or y < 0:
            return float("inf")
        if self.chart[x][y] != None:
            return self.chart[x][y]
        add = 1
        if self.word1[y] == self.word2[x]:
            add = 0
        num = min(self.getValue(x - 1, y) + 1, self.getValue(x, y - 1) + 1, self.getValue(x - 1, y - 1) + add)
        if num < abs(x - y):
            num = abs(x - y)
        self.chart[x][y] = num
        return num 


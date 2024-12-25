import copy


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        chart = []
        word1 = " " + word1
        word2 = " " + word2
        for i in range(len(word2)):
            chart.append([float("inf")] * (len(word1)))
        chart[0][0] = 0
        for i in range(len(word2)):
            for j in range(len(word1)):
                if i == 0 and j == 0:
                    continue
                add = 1
                if word1[j] == word2[i]:
                    add = 0
                chart[i][j] = min(
                    chart[i - 1][j] + 1, chart[i][j - 1] + 1, chart[i - 1][j - 1] + add
                )
        return chart[len(word2) - 1][len(word1) - 1]

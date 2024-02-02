import copy


class Solution:
    def maxArea(self, height: List[int]) -> int:
        best = self.count(height)
        left = height[0 : best[0] + 1]
        right = height[best[1] : len(height)]
        for i in range(len(left)):
            for j in range(len(right)):
                if (best[1] + j - i) * min(left[i], right[j]) > best[2]:
                    best[2] = (best[1] + j - i) * min(left[i], right[j])
        return best[2]

    def count(self, height):
        li = []
        for i in range(len(height)):
            li.append([height[i], i])
        li.sort(reverse=True)
        best = [
            min(li[1][1], li[0][1]),
            max(li[1][1], li[0][1]),
            min(li[1][0], li[0][0]) * abs(li[0][1] - li[1][1]),
        ]
        for i in range(2, len(height)):
            if li[i][1] < best[0]:
                if min(li[i][0], height[best[1]]) * abs(li[i][1] - best[1]) >= best[2]:
                    best[0] = li[i][1]
                    best[2] = min(li[i][0], height[best[1]]) * abs(li[i][1] - best[1])

            if li[i][1] > best[1]:
                if min(li[i][0], height[best[0]]) * abs(li[i][1] - best[0]) >= best[2]:
                    best[1] = li[i][1]
                    best[2] = min(li[i][0], height[best[0]]) * abs(li[i][1] - best[0])
        return best

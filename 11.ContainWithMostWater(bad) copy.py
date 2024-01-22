import copy


class Solution:
    def maxArea(self, height: List[int]) -> int:
        print(height)
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
        heightIndex = []
        for i in range(len(height)):
            li.append([height[i], i])
        li.sort()
        for i in li:
            heightIndex.append(i[1])
        heightIndex.reverse()
        heightS = copy.deepcopy(height)
        heightS.sort()
        heightS.reverse()
        best = [
            min(heightIndex[1], heightIndex[0]),
            max(heightIndex[1], heightIndex[0]),
            min(heightS[1], heightS[0]) * abs(heightIndex[0] - heightIndex[1]),
        ]
        for i in range(2, len(height)):
            if heightIndex[i] < best[0]:
                if (
                    min(heightS[i], height[best[1]]) * abs(heightIndex[i] - best[1])
                    >= best[2]
                ):
                    best[0] = heightIndex[i]
                    best[2] = min(heightS[i], height[best[1]]) * abs(
                        heightIndex[i] - best[1]
                    )

            if heightIndex[i] > best[1]:
                if (
                    min(heightS[i], height[best[0]]) * abs(heightIndex[i] - best[0])
                    >= best[2]
                ):
                    best[1] = heightIndex[i]
                    best[2] = min(heightS[i], height[best[0]]) * abs(
                        heightIndex[i] - best[0]
                    )

            print(best)
        return best

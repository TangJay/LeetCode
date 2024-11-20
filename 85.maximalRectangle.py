class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = 0
        heights = [0] * (len(matrix[0]))
        print(heights)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heights[j] = (heights[j] + 1) * int(matrix[i][j])
            ans = max(ans, self.calculate(heights))
        return ans

    def calculate(self, heights):
        stack = []
        area = 0
        heights.append(0)
        for index in range(len(heights)):
            value = heights[index]
            while stack and heights[stack[-1]] > value:
                lowestIndex = stack.pop()
                lowestValue = heights[lowestIndex]
                width = index - stack[-1] - 1 if stack else index
                area = max(area, width * lowestValue)
            stack.append(index)
        return area

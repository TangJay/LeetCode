class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
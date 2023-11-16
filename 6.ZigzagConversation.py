class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = []
        for i in range(numRows):
            rows.append([])
        value = 0
        increaseValue = 1
        for i in s:
            rows[value].append(i)
            value += increaseValue
            if value == numRows - 1:
                increaseValue = -1
            if value == 0:
                increaseValue = 1
        finalList = []
        for i in rows:
            finalList += i
        return "".join(finalList)

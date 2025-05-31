class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for i in range(n):
            matrix.append([])
            for j in range(n):
                matrix[i].append(None)
        time = 0
        place = [0, -1]
        num = 1
        add = 1
        while time + 1 <= n:
            for i in range(n - time):
                place[1] += add
                matrix[place[0]][place[1]] = num
                num += 1
            for i in range(n - time - 1):
                place[0] += add
                matrix[place[0]][place[1]] = num
                num += 1
            add *= -1
            time += 1
        return matrix

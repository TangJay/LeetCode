class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x = len(matrix)
        y = len(matrix[0])
        moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        turn = 0
        coordinates = [0, 0]
        ans = [matrix[0][0]]
        temp = 1
        while len(ans) != x * y:
            for i in range(y - 2 * turn - temp):
                if len(ans) == x * y:
                    break
                print("aa")
                coordinates[1] += 1
                ans.append(matrix[coordinates[0]][coordinates[1]])
            for i in range(x - 1 - 2 * turn):
                if len(ans) == x * y:
                    break
                coordinates[0] += 1
                ans.append(matrix[coordinates[0]][coordinates[1]])
            for i in range(y - 1 - 2 * turn):
                if len(ans) == x * y:
                    break
                coordinates[1] -= 1
                ans.append(matrix[coordinates[0]][coordinates[1]])
            for i in range(x - 2 - 2 * turn):
                if len(ans) == x * y:
                    break
                coordinates[0] -= 1
                ans.append(matrix[coordinates[0]][coordinates[1]])
            turn += 1
            temp = 0
        return ans

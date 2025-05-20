class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        if n % 2 == 1:
            x = (n - 1) // 2
            y = (n + 1) // 2
        else:
            x = n // 2
            y = x
        for i in range(x):
            for j in range(y):
                (
                    matrix[j][n - i - 1],
                    matrix[n - i - 1][n - j - 1],
                    matrix[n - j - 1][i],
                    matrix[i][j],
                ) = (
                    matrix[i][j],
                    matrix[j][n - i - 1],
                    matrix[n - i - 1][n - j - 1],
                    matrix[n - j - 1][i],
                )
        print(matrix)

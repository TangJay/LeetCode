import copy
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        blanks = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    blanks.append([i, j])
        result = self.rotate(board, blanks)
        return result
    def rotate(self, board, blanks):
        able = self.search(blanks[0][0], blanks[0][1], board)
        if len(able) == 0:
            return False
        for i in able:
            board[blanks[0][0]][blanks[0][1]] = i
            if len(blanks) == 1:
                return board
            blanksC = copy.deepcopy(blanks)
            blanksC.pop(0)
            result = self.rotate(board, blanksC)
            if result == False:
                board[blanks[0][0]][blanks[0][1]] = "."
                continue
            return result
        return False
    def search(self, x, y, board):
        able = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(9):
            if board[x][i] in able:
                able.remove(board[x][i])
        for i in range(9):
            if board[i][y] in able:
                able.remove(board[i][y])
        baseX = (x // 3) * 3
        baseY = (y // 3) * 3
        for i in range(baseX, baseX + 3):
            for j in range(baseY, baseY + 3):
                if board[i][j] in able:
                    able.remove(board[i][j])
        return able
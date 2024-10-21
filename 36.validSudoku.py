class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            temp = []
            for j in range(9):
                if i[j].isdigit() == True:
                    if i[j] in temp:
                        return False
                    temp.append(i[j])
        for i in range(9):
            temp = []
            for j in board:
                if j[i].isdigit() == True:
                    if j[i] in temp:
                        return False
                    temp.append(j[i])
        for i in range(9):
            temp = []
            for j in range(3 * (i // 3), 3 * (i // 3 + 1)):
                for k in range(3 * (i % 3), 3 * (i % 3 + 1)):
                    if board[j][k].isdigit() == True:
                        if board[j][k] in temp:
                            return False
                        temp.append(board[j][k])
        return True
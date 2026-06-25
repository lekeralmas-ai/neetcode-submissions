class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            num_s = set()
            for i in range(9):
                if board[row][i] == '.':
                    continue
                if board[row][i] in num_s:
                    return False
                num_s.add(board[row][i])
        for col in range(9):
            num_s1 = set()
            for i in range(9):
                if board[i][col] == '.':
                    continue
                if board[i][col] in num_s1:
                    return False
                num_s1.add(board[i][col])
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3)*3 + i 
                    column = (square%3)*3 +j
                    if board[row][column] == '.':
                        continue
                    if board[row][column] in seen:
                        return False
                    seen.add(board[row][column])
        return True
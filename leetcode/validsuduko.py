class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            rowset = set()
            for j in range(len(board[0])):
                if board[i][j] in rowset:
                    return False
                if board[i][j] == ".":
                    continue
                else:
                    rowset.add(board[i][j])
        for i in range(len(board[0])):
            colset = set()
            for j in range(len(board)):
                if board[j][i] in colset:
                    return False
                if board[j][i] == ".":
                    continue
                else:
                    colset.add(board[j][i])

        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                subboxset = set()
                for a in range(3):
                    for b in range(3):
                        if board[i + a][j + b] in subboxset:
                            return False
                        if board[i + a][j + b] == ".":
                            continue
                        else:
                            subboxset.add(board[i + a][j + b])
        return True

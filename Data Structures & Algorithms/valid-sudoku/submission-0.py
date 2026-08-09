class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: set() for i in range(9)}
        cols = {j: set() for j in range(9)}
        boxes = {(i,j): set() for i in range(9) for j in range(9)}

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                if ((value in rows[i]) or (value in cols[j]) or (value in boxes[i//3,j//3])):
                    return False
                rows[i].add(value)
                cols[j].add(value)
                boxes[i//3,j//3].add(value)
        return True 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=set()
        for r in range(9):
            for c in range(9):
                value=board[r][c]
                if value!=".":
                    row=(r,value)
                    column=(value,c)
                    box=(r//3,c//3,value)
                    if row in seen or column in seen or box in seen:
                        return False
                    seen.add(row)
                    seen.add(column)
                    seen.add(box)
        return True
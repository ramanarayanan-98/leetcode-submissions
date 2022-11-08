class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsets = [set() for _ in range(9)]
        colsets = [set() for _ in range(9)]
        squaresets = [[set() for _ in range(3)] for _ in range(3)]
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                
                if val in rowsets[i] or val in colsets[j] or val in squaresets[i//3][j//3]:
                    return False
                
                rowsets[i].add(val)
                colsets[j].add(val)
                squaresets[i//3][j//3].add(val)
        
        return True
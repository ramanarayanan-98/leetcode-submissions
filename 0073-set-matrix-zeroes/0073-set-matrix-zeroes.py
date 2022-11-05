class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix),len(matrix[0])
        isFirstColZero = False
        for i in range(m):
            if not matrix[i][0]:
                isFirstColZero = True
            for j in range(1,n):
                if matrix[i][j]:
                    continue
                matrix[i][0] = 0
                matrix[0][j] = 0
        
        for i in range(1,m):
            for j in range(1,n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        
        if not matrix[0][0]:
            for j in range(1,n):
                matrix[0][j] = 0
        
        if isFirstColZero:
            for i in range(m):
                matrix[i][0] = 0
        
        
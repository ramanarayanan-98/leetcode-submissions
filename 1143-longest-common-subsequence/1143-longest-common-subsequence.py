class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)
        dpmat = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dpmat[i][j] = 1+dpmat[i-1][j-1]
                else:
                    dpmat[i][j] = max(dpmat[i-1][j],dpmat[i][j-1])
                
        
        return dpmat[m][n]
                        
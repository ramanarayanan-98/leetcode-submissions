class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)
        dpmat = [0 for _ in range(n+1)]
        for i in range(1,m+1):
            prev = 0
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    prev,dpmat[j] = dpmat[j],1+prev
                else:
                    prev,dpmat[j] = dpmat[j],max(dpmat[j],dpmat[j-1])
        
        return dpmat[n]
                        
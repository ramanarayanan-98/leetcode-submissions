class Solution:
    def uniquePathHelper(self,m,n):
        prod = 1
        for i in range(m+1,m+n+1):
            prod *= i
            prod /= (i-m)
        return int(prod)
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        if m < n:
            m,n = n,m
        
        return self.uniquePathHelper(m,n)
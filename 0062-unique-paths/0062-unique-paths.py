class Solution:
    def fact(self,num):
        prod = 1
        for i in range(num,1,-1):
            prod *= i
        return prod
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        return self.fact(m+n)//(self.fact(m)*self.fact(n))
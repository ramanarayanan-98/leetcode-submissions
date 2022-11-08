class Solution:
    def climbStairs(self, n: int) -> int:
        a,b = 1,1
        if n <= 1:
            return n
        
        n -= 1
        
        while n:
            a,b = b,a+b
            n -= 1
        
        return b
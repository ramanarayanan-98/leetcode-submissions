class Solution:
    def numTilings(self, n: int) -> int:
        a,b,c = 1,2,5
        if n <= 2:
            return n
        n -= 3
        while n:
            temp = (2*c)+a
            a = b
            b = c
            c = int(temp%(math.pow(10,9)+7))
            n -= 1
        
        return c
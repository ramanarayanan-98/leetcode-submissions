class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            sod = 0
            while n:
                d = n%10
                n //= 10
                sod += d*d
            n = sod
        
        return n == 1
                    
        
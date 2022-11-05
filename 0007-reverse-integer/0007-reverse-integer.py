class Solution:
    def reverse(self, x: int) -> int:
        twop31 = 2**31
        pmaxlimit = twop31-1
        nmaxlimit = -twop31
        res = 0
        while x:
            d = int(math.fmod(x,10))
            x = int(x/10)
            if res > pmaxlimit//10 or (res == pmaxlimit//10 and d > 7):
                return 0
            if res < int(nmaxlimit/10) or (res == int(nmaxlimit/10) and d < -8):
                return 0
            res = res*10 + d
            
        
        return res
            
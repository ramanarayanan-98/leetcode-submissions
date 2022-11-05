class Solution:
    def reverse(self, x: int) -> int:
        twop31 = 2**31
        pmaxlimit = twop31-1
        nmaxlimit = -twop31
        isNeg = x < 0
        x = -x if isNeg else x
        res = 0
        while x:
            d = x%10
            x //= 10
            res = res*10 + d
            if res > pmaxlimit:
                return 0
        
        return res if not isNeg else -res
            
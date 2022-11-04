class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        if n == 0:
            return res
        
        count = 1
        
        for i in range(1,n+1):
            if count*2 == i:
                count = i
            res.append(res[i-count]+1)
        
        return res
                
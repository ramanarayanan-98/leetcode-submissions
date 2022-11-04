class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res = [0,1]
        if n == 1:
            return res
            
        count = 2
        
        for i in range(2,n+1):
            if count*2 == i:
                count = i
            res.append(res[i-count]+1)
        
        return res
                
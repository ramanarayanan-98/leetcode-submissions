class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res = [0,1]
        if n == 1:
            return res
            
        count = 2
        
        while len(res) < n+1:
            for _ in range(count):
                if len(res) == n+1:
                    break
                res.append(res[len(res)-count]+1)
            count *= 2
            
            
        
        return res
                
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            count = 0
            while i:
                if i < len(res):
                    count += res[i]
                    break
                count += 1
                i &= i-1
            res.append(count)
        
        return res
                
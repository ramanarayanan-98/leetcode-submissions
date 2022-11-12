class Solution:
    def calcEatingHours(self,piles,mid):
        hours = 0
        
        for pile in piles:
            hours += math.ceil(pile/mid)
        
        return hours
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo,hi = 1,max(piles)
        
        while lo < hi:
            mid = lo + (hi-lo)//2
            
            if self.calcEatingHours(piles,mid) <= h:
                hi = mid
            else:
                lo = mid+1
        
        return lo
            
            
        
        
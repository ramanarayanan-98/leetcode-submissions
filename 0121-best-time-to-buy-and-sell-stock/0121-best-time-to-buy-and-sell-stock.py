class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minTillNow = float("inf")
        maxProfit = 0
        
        for price in prices:
            maxProfit = max(maxProfit,price-minTillNow)
            minTillNow = min(minTillNow,price)
        
        return maxProfit
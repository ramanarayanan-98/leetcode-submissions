class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minTillNow = float("inf")
        maxProfit = 0
        
        for price in prices:
            if price >= minTillNow:
                maxProfit = max(maxProfit,price-minTillNow)
            else:
                minTillNow = price
        
        return maxProfit
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        rightMax = [0 for _ in range(n)]
        maxTillNow = 0
        for i in range(n-1,-1,-1):
            rightMax[i] = maxTillNow
            maxTillNow = max(maxTillNow,height[i])
        
        maxTillNow = 0
        trapArea = 0
        
        for i in range(n):
            value = min(maxTillNow,rightMax[i])-height[i]
            trapArea += value if value > 0 else 0
            maxTillNow = max(maxTillNow,height[i])
        
        return trapArea
            
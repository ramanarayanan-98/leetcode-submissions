class Solution:
    def maxArea(self, height: List[int]) -> int:
        start,end = 0,len(height)-1
        maxArea = 0
        
        while start < end:
            maxArea = max(maxArea,(end-start)*min(height[start],height[end]))
            
            if min(height[start],height[end]) == height[start]:
                start += 1
            else:
                end -= 1
        return maxArea
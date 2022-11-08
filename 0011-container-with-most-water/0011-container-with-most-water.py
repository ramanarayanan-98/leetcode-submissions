class Solution:
    def maxArea(self, height: List[int]) -> int:
        start,end = 0,len(height)-1
        maxArea = 0
        
        while start < end:
            diff = end-start
            if height[start] <= height[end]:
                maxArea = max(maxArea,diff*height[start])
                start += 1
            else:
                maxArea = max(maxArea,diff*height[end])
                end -= 1
        return maxArea
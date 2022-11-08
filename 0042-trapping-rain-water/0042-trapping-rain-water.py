class Solution:
    def trap(self, height: List[int]) -> int:
        start,end = 0,len(height)-1
        trapArea,leftmax,rightmax = 0,0,0
        
        while start < end:
            if height[start] <= height[end]:
                if height[start] >= leftmax:
                    leftmax = height[start]
                else:
                    trapArea += (leftmax-height[start])
                start += 1
            else:
                if height[end] >= rightmax:
                    rightmax = height[end]
                else:
                    trapArea += (rightmax-height[end])
                end -= 1
        
        return trapArea
            
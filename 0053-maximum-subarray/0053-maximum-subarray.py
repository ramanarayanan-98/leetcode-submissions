class Solution:
    def maxSumSubArrayHelper(self,nums,s,e):
        if s == e:
            return nums[s]
        
        mid = s+(e-s)//2
        
        curSum = 0
        maxLeft = float("-inf")
        for i in range(mid,s-1,-1):
            curSum += nums[i]
            maxLeft = max(maxLeft,curSum)
        
        curSum = 0
        maxRight = float("-inf")
        for i in range(mid+1,e+1):
            curSum += nums[i]
            maxRight = max(maxRight,curSum)
        
        combined = maxLeft+maxRight if maxLeft != float("-inf") and maxRight != float("-inf") else max(maxLeft,maxRight)
        return max(self.maxSumSubArrayHelper(nums,s,mid),self.maxSumSubArrayHelper(nums,mid+1,e),combined)
    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxSumSubArrayHelper(nums,0,len(nums)-1)
        
        
        
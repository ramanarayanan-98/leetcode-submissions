class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = nums[0]
        maxSum = curSum
        
        for i in range(1,len(nums)):
            if curSum + nums[i] < nums[i]:
                curSum = nums[i]
            else:
                curSum += nums[i]
            maxSum = max(maxSum,curSum)
        return maxSum
        
        
        
class Solution:
    def rob(self, nums: List[int]) -> int:
        prevMaxCost = 0
        curMaxCost = nums[0]
        
        for i in range(1,len(nums)):
            prevMaxCost, curMaxCost = curMaxCost, max(prevMaxCost+nums[i],curMaxCost)
        
        return max(prevMaxCost,curMaxCost)
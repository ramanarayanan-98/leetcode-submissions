class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numIdxSet = set(nums)
        maxcount = 0
        
        for i in range(len(nums)):
            if nums[i]-1 in numIdxSet:
                continue
            
            curval = nums[i]
            count = 1
            
            while curval+1 in numIdxSet:
                count += 1
                curval += 1
            
            maxcount = max(maxcount,count)
        
        return maxcount
            
            
            
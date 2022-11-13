class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numIdxSet = set(nums)
        visited = set()
        maxcount = 0
        
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            
            curval = nums[i]
            visited.add(curval)
            count = 1
            
            while curval-1 in numIdxSet:
                count += 1
                visited.add(curval-1)
                curval -= 1
            
            curval = nums[i]
            while curval+1 in numIdxSet:
                count += 1
                visited.add(curval+1)
                curval += 1
            
            maxcount = max(maxcount,count)
        
        return maxcount
            
            
            
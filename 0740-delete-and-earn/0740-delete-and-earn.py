import collections
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        values = [0]*(max(nums)+1)
        for num in nums:
            values[num] += num
        take,skip = 0,0
        for i in range(0,max(nums)+1):
            takei = skip + values[i]
            skipi = max(take,skip)
            take,skip = takei,skipi
        
        return max(take,skip)
        
        
    
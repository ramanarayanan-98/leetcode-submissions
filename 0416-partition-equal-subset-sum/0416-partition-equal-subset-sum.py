class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalsum = sum(nums)
        n = len(nums)
        if totalsum%2:
            return False
        totalsum //= 2
        cache = [False for _ in range(totalsum+1)]
        cache[0] = True
        
        for i in range(1,n+1):
            for j in range(totalsum,-1,-1):
                if j >= nums[i-1]:
                    cache[j] |= cache[j-nums[i-1]]
        return cache[-1]
        
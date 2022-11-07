class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalsum = sum(nums)
        n = len(nums)
        if totalsum%2:
            return False
        totalsum //= 2
        cache = [[False for _ in range(totalsum+1)] for _ in range(n+1)]
        for i in range(n+1):
            cache[i][0] = True
        
        for i in range(1,n+1):
            for j in range(1,totalsum+1):
                if j < nums[i-1]:
                    cache[i][j] = cache[i-1][j]
                else:
                    cache[i][j] = cache[i-1][j] | cache[i-1][j-nums[i-1]]
        return cache[-1][-1]
        
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxpossible = 0
        for i in range(n):
            if i > maxpossible:
                break
            if i <= maxpossible and i+nums[i] > maxpossible:
                maxpossible = i+nums[i]
        return maxpossible >= n-1            
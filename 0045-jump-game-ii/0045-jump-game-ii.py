class Solution:
    def jump(self, nums: List[int]) -> int:
        maxJumpIdx,steps,pos = 0,0,0
        
        while maxJumpIdx < len(nums)-1:
            nextMax = maxJumpIdx
            for i in range(pos,maxJumpIdx+1):
                nextMax = max(nextMax,i+nums[i])
            if maxJumpIdx == nextMax:
                return -1
            pos = maxJumpIdx+1
            maxJumpIdx = nextMax
            steps += 1
        
        return steps
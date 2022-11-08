class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsset = collections.defaultdict(int)
        for i,num in enumerate(nums):
            if target-num in numsset:
                return [numsset[target-num],i]
            numsset[num] = i
        return [-1,-1]
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xorres = 0
        for num in nums:
            xorres ^= num
        
        return xorres
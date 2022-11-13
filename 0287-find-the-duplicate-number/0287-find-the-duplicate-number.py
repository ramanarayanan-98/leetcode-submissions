class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l,r = 1,len(nums)-1
        
        while l < r:
            m = (l+r)//2
            
            count = sum(num <= m for num in nums)
            # print(l,m,r,count)
            if count > m:
                r = m
            else:
                l = m+1
        
        return l
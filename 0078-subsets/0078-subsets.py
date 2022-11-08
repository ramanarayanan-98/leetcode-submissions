class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            restemp = []
            for sub in res:
                temp = list(sub)
                temp.append(num)
                restemp.append(temp)
            res.extend(restemp)
        
        return res
            
            
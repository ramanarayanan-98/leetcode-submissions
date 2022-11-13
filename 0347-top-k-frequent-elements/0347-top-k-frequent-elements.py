class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCount = collections.Counter(nums)
        bucket = [list() for _ in range(len(nums))]
        
        for num in numsCount:
            bucket[numsCount[num]-1].append(num)
        
        res = []
        i = len(nums)-1
        while i >= 0 and len(res) < k:
            if len(res)+len(bucket[i]) <= k:
                res.extend(bucket[i])
            else:
                j = 0
                while j < len(bucket[i]) and len(res) < k:
                    res.append(bucket[i][j])
                    j += 1
                    
            i -= 1
        
        return res